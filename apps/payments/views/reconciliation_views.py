from rest_framework import viewsets, permissions
from ..models import PaymentReconciliation
from ..serializers.reconciliation_serializers import PaymentReconciliationSerializer

class PaymentReconciliationViewSet(viewsets.ModelViewSet):
    queryset = PaymentReconciliation.objects.all()
    serializer_class = PaymentReconciliationSerializer
    permission_classes = [permissions.IsAdminUser]