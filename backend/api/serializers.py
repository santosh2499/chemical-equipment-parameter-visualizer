from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Dataset, EquipmentData


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']
    
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class EquipmentDataSerializer(serializers.ModelSerializer):
    """Serializer for EquipmentData model"""
    class Meta:
        model = EquipmentData
        fields = ['id', 'equipment_name', 'equipment_type', 'flowrate', 'pressure', 'temperature']
        read_only_fields = ['id']


class DatasetSerializer(serializers.ModelSerializer):
    """Serializer for Dataset model"""
    user = UserSerializer(read_only=True)
    equipment = EquipmentDataSerializer(many=True, read_only=True)
    equipment_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Dataset
        fields = [
            'id', 'user', 'name', 'file', 'uploaded_at',
            'total_count', 'avg_flowrate', 'avg_pressure', 'avg_temperature',
            'equipment_types', 'equipment', 'equipment_count'
        ]
        read_only_fields = ['id', 'uploaded_at', 'total_count', 'avg_flowrate', 
                           'avg_pressure', 'avg_temperature', 'equipment_types']
    
    def get_equipment_count(self, obj):
        return obj.equipment.count()


class DatasetListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing datasets"""
    user = UserSerializer(read_only=True)
    equipment_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Dataset
        fields = [
            'id', 'user', 'name', 'uploaded_at',
            'total_count', 'avg_flowrate', 'avg_pressure', 'avg_temperature',
            'equipment_types', 'equipment_count'
        ]
        read_only_fields = ['id', 'uploaded_at']
    
    def get_equipment_count(self, obj):
        return obj.equipment.count()


class DatasetUploadSerializer(serializers.Serializer):
    """Serializer for CSV file upload"""
    file = serializers.FileField()
    name = serializers.CharField(max_length=255, required=False)
    
    def validate_file(self, value):
        if not value.name.endswith('.csv'):
            raise serializers.ValidationError("Only CSV files are allowed")
        
        # Check file size (5MB max)
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("File size must be less than 5MB")
        
        return value
