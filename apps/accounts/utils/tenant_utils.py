from ..models import Tenant
from decimal import Decimal

def calculate_tenant_balance(tenant: Tenant) -> Decimal:
    """Calculate the current balance for a tenant"""
    total_payments = tenant.payment_set.filter(
        status='completed'
    ).aggregate(
        total=models.Sum('amount')
    )['total'] or Decimal('0')
    
    return tenant.balance - total_payments

def get_tenant_by_reference(reference: str) -> Tenant:
    """Get tenant by reference number"""
    try:
        return Tenant.objects.get(reference_number=reference)
    except Tenant.DoesNotExist:
        return None