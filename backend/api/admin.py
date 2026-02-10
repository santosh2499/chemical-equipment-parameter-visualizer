from django.contrib import admin
from .models import Dataset, EquipmentData


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'total_count', 'uploaded_at']
    list_filter = ['uploaded_at', 'user']
    search_fields = ['name', 'user__username']
    readonly_fields = ['uploaded_at', 'total_count', 'avg_flowrate', 'avg_pressure', 'avg_temperature']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'name', 'file', 'uploaded_at')
        }),
        ('Statistics', {
            'fields': ('total_count', 'avg_flowrate', 'avg_pressure', 'avg_temperature', 'equipment_types')
        }),
    )


@admin.register(EquipmentData)
class EquipmentDataAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'equipment_type', 'flowrate', 'pressure', 'temperature', 'dataset']
    list_filter = ['equipment_type', 'dataset']
    search_fields = ['equipment_name', 'equipment_type']
    
    fieldsets = (
        ('Equipment Information', {
            'fields': ('dataset', 'equipment_name', 'equipment_type')
        }),
        ('Parameters', {
            'fields': ('flowrate', 'pressure', 'temperature')
        }),
    )
