from rest_framework import serializers
from ..models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    tenant_name = serializers.CharField(source='tenant.user.username', read_only=True)
    property_name = serializers.CharField(source='tenant.property_manager.company_name', read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'tenant', 'tenant_name', 'property_name', 'amount', 
                 'payment_type', 'status', 'reference', 'transaction_id', 
                 'created_at']