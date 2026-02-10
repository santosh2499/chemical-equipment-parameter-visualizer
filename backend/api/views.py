from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Avg, Count
from .models import Dataset, EquipmentData
from .serializers import (
    UserSerializer, UserRegistrationSerializer,
    DatasetSerializer, DatasetListSerializer,
    EquipmentDataSerializer, DatasetUploadSerializer
)
from .utils import process_csv_file, generate_pdf_report
import pandas as pd
import json


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Register a new user"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'message': 'User registered successfully',
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """Login user"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({
            'error': 'Please provide both username and password'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return Response({
            'message': 'Login successful',
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'error': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """Logout user"""
    logout(request)
    return Response({
        'message': 'Logout successful'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def current_user(request):
    """Get current logged-in user"""
    if request.user.is_authenticated:
        return Response(UserSerializer(request.user).data)
    else:
        return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


class DatasetViewSet(viewsets.ModelViewSet):
    """ViewSet for Dataset operations"""
    # Using default permission classes from settings (AllowAny)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return DatasetListSerializer
        return DatasetSerializer
    
    def get_queryset(self):
        # Return only user's datasets
        if self.request.user.is_authenticated:
            return Dataset.objects.filter(user=self.request.user)
        return Dataset.objects.none()
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    @csrf_exempt
    def upload(self, request):
        """Upload and process CSV file"""
        # Require authentication for upload
        if not request.user.is_authenticated:
            return Response({
                'error': 'Authentication required. Please login to upload datasets.'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = DatasetUploadSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        file = serializer.validated_data['file']
        name = serializer.validated_data.get('name', file.name)
        
        try:
            # Process CSV file
            df = pd.read_csv(file)
            
            # Validate required columns
            required_columns = ['Equipment Name', 'Type', 'Flowrate', 'Pressure', 'Temperature']
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                return Response({
                    'error': f'Missing required columns: {", ".join(missing_columns)}'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Create dataset with authenticated user
            dataset = Dataset.objects.create(
                user=request.user,
                name=name,
                file=file
            )
            
            # Process and save equipment data
            equipment_list = []
            equipment_types = {}
            
            for _, row in df.iterrows():
                equipment = EquipmentData(
                    dataset=dataset,
                    equipment_name=row['Equipment Name'],
                    equipment_type=row['Type'],
                    flowrate=float(row['Flowrate']),
                    pressure=float(row['Pressure']),
                    temperature=float(row['Temperature'])
                )
                equipment_list.append(equipment)
                
                # Count equipment types
                eq_type = row['Type']
                equipment_types[eq_type] = equipment_types.get(eq_type, 0) + 1
            
            # Bulk create equipment records
            EquipmentData.objects.bulk_create(equipment_list)
            
            # Calculate and save statistics
            dataset.total_count = len(equipment_list)
            dataset.avg_flowrate = df['Flowrate'].mean()
            dataset.avg_pressure = df['Pressure'].mean()
            dataset.avg_temperature = df['Temperature'].mean()
            dataset.equipment_types = equipment_types
            dataset.save()
            
            return Response({
                'message': 'File uploaded and processed successfully',
                'dataset': DatasetSerializer(dataset).data
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            # Clean up if something went wrong
            if 'dataset' in locals():
                dataset.delete()
            
            return Response({
                'error': f'Error processing file: {str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def summary(self, request, pk=None):
        """Get dataset summary statistics"""
        dataset = self.get_object()
        
        # Get equipment type distribution
        type_distribution = []
        for eq_type, count in dataset.equipment_types.items():
            type_distribution.append({
                'type': eq_type,
                'count': count,
                'percentage': round((count / dataset.total_count) * 100, 2)
            })
        
        # Get parameter ranges
        equipment = dataset.equipment.all()
        
        summary = {
            'dataset_id': dataset.id,
            'dataset_name': dataset.name,
            'uploaded_at': dataset.uploaded_at,
            'total_count': dataset.total_count,
            'statistics': {
                'flowrate': {
                    'average': round(dataset.avg_flowrate, 2),
                    'min': round(equipment.aggregate(min=models.Min('flowrate'))['min'], 2) if equipment.exists() else 0,
                    'max': round(equipment.aggregate(max=models.Max('flowrate'))['max'], 2) if equipment.exists() else 0,
                },
                'pressure': {
                    'average': round(dataset.avg_pressure, 2),
                    'min': round(equipment.aggregate(min=models.Min('pressure'))['min'], 2) if equipment.exists() else 0,
                    'max': round(equipment.aggregate(max=models.Max('pressure'))['max'], 2) if equipment.exists() else 0,
                },
                'temperature': {
                    'average': round(dataset.avg_temperature, 2),
                    'min': round(equipment.aggregate(min=models.Min('temperature'))['min'], 2) if equipment.exists() else 0,
                    'max': round(equipment.aggregate(max=models.Max('temperature'))['max'], 2) if equipment.exists() else 0,
                }
            },
            'type_distribution': type_distribution
        }
        
        return Response(summary)
    
    @action(detail=True, methods=['get'])
    def report(self, request, pk=None):
        """Generate PDF report for dataset"""
        dataset = self.get_object()
        
        try:
            pdf_buffer = generate_pdf_report(dataset)
            
            response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="equipment_report_{dataset.id}.pdf"'
            
            return response
            
        except Exception as e:
            return Response({
                'error': f'Error generating report: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Import models for aggregation
from django.db import models
