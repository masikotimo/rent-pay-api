from django.db import models
from apps.accounts.models import PropertyManager

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    property_manager = models.ForeignKey(PropertyManager, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'properties'

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=20)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_occupied = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'units'
        unique_together = ('property', 'unit_number')