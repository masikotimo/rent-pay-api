from django.db import models
from apps.accounts.models import Tenant

class USSDSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)
    current_menu = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'ussd_sessions'

class USSDLog(models.Model):
    session = models.ForeignKey(USSDSession, on_delete=models.CASCADE)
    input = models.CharField(max_length=255)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'ussd_logs'