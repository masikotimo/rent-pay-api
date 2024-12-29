from django.db import models
from apps.accounts.models import Tenant

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    PAYMENT_TYPE_CHOICES = (
        ('ussd', 'USSD'),
        ('bank_transfer', 'Bank Transfer'),
    )
    
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    reference = models.CharField(max_length=100, unique=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'payments'

class PaymentReconciliation(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    bank_reference = models.CharField(max_length=100)
    reconciled_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'payment_reconciliations'