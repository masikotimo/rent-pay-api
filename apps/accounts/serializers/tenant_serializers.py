from rest_framework import serializers
from ..models import Tenant, User
from ..utils.reference_generator import generate_tenant_reference
from apps.payments.serializers.payment_serializers import PaymentSerializer

class TenantCreateSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()
    name = serializers.CharField()  # Changed from username to name for clarity

    class Meta:
        model = Tenant
        fields = ['name', 'phone_number']

    def create(self, validated_data):
        name = validated_data.pop('name')
        phone_number = validated_data.pop('phone_number')
        
        # Create user without password
        user = User.objects.create(
            username=name.lower().replace(' ', '_'),  # Generate username from name
            phone_number=phone_number,
            user_type='tenant',
            is_active=False  # Disable login since tenants don't need it
        )
        
        # Get property manager from context
        property_manager = self.context['property_manager']
        
        # Generate unique reference number
        reference_number = generate_tenant_reference()
        while Tenant.objects.filter(reference_number=reference_number).exists():
            reference_number = generate_tenant_reference()
        
        tenant = Tenant.objects.create(
            user=user,
            property_manager=property_manager,
            reference_number=reference_number
        )
        
        return tenant

class TenantDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username')
    phone_number = serializers.CharField(source='user.phone_number')
    recent_payments = PaymentSerializer(many=True, read_only=True)
    total_balance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'phone_number', 'reference_number', 
                 'balance', 'recent_payments', 'total_balance']