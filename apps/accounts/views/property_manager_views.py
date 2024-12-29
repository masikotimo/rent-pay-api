from rest_framework import viewsets, permissions
from rest_framework.response import Response
from ..models import PropertyManager
from ..serializers.property_manager_serializers import (
    PropertyManagerCreateSerializer,
    PropertyManagerDetailSerializer
)

class PropertyManagerViewSet(viewsets.ModelViewSet):
    queryset = PropertyManager.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'create':
            return PropertyManagerCreateSerializer
        return PropertyManagerDetailSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'property_manager':
            return PropertyManager.objects.filter(user=self.request.user)
        return super().get_queryset()