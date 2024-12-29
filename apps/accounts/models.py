from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('property_manager', 'Property Manager'),
        ('tenant', 'Tenant'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

class PropertyManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'property_managers'

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=20, unique=True)
    property_manager = models.ForeignKey(PropertyManager, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        db_table = 'tenants'