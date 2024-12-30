from rest_framework import viewsets, permissions
from ..models import Payment
from ..serializers.payment_serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'property_manager':
            # return Payment.objects.filter(tenant__property_manager=self.request.user.propertymanager)
            return Payment.objects.all()
        elif self.request.user.user_type == 'tenant':
            return Payment.objects.filter(tenant__user=self.request.user)
        return super().get_queryset()