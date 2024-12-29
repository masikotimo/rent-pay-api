from rest_framework import serializers
from ..models import PaymentReconciliation
from .payment_serializers import PaymentSerializer

class PaymentReconciliationSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(read_only=True)
    payment_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PaymentReconciliation
        fields = ['id', 'payment', 'payment_id', 'bank_reference', 'reconciled_at']
        read_only_fields = ['reconciled_at']

    def create(self, validated_data):
        payment_id = validated_data.pop('payment_id')
        validated_data['payment_id'] = payment_id
        return super().create(validated_data)