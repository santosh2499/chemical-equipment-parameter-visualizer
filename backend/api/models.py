from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import json


class Dataset(models.Model):
    """Model to store uploaded datasets"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='datasets')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # Store summary statistics as JSON
    total_count = models.IntegerField(default=0)
    avg_flowrate = models.FloatField(default=0.0)
    avg_pressure = models.FloatField(default=0.0)
    avg_temperature = models.FloatField(default=0.0)
    equipment_types = models.JSONField(default=dict)  # Store type distribution
    
    class Meta:
        ordering = ['-uploaded_at']
        
    def __str__(self):
        return f"{self.name} - {self.user.username}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Clean up old datasets if more than MAX_DATASETS
        user_datasets = Dataset.objects.filter(user=self.user).order_by('-uploaded_at')
        max_datasets = getattr(settings, 'MAX_DATASETS', 5)
        
        if user_datasets.count() > max_datasets:
            # Delete oldest datasets
            datasets_to_delete = user_datasets[max_datasets:]
            for dataset in datasets_to_delete:
                # Delete the file as well
                if dataset.file:
                    dataset.file.delete()
                dataset.delete()


class EquipmentData(models.Model):
    """Model to store individual equipment records"""
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='equipment')
    equipment_name = models.CharField(max_length=255)
    equipment_type = models.CharField(max_length=100)
    flowrate = models.FloatField()
    pressure = models.FloatField()
    temperature = models.FloatField()
    
    class Meta:
        ordering = ['equipment_name']
        
    def __str__(self):
        return f"{self.equipment_name} ({self.equipment_type})"
