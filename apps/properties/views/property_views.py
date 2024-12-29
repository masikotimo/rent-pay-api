from rest_framework import viewsets, permissions
from ..models import Property
from ..serializers.property_serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_queryset(self):
        if self.request.user.user_type == 'property_manager':
            return Property.objects.filter(property_manager=self.request.user.propertymanager)
        return super().get_queryset()