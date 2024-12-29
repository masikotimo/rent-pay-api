from rest_framework import viewsets, permissions
from ..models import Unit
from ..serializers.unit_serializers import UnitSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'property_manager':
            return Unit.objects.filter(property__property_manager=self.request.user.propertymanager)
        return super().get_queryset()