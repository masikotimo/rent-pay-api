from rest_framework import viewsets, permissions
from rest_framework.response import Response
from ..models import Tenant
from ..serializers.tenant_serializers import (
    TenantCreateSerializer,
    TenantDetailSerializer
)

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return TenantCreateSerializer
        return TenantDetailSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'property_manager':
            # return Tenant.objects.filter(property_manager=self.request.user.propertymanager)
            return Tenant.objects.all()
        elif self.request.user.user_type == 'tenant':
            return Tenant.objects.filter(user=self.request.user)
        return super().get_queryset()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.user.user_type == 'property_manager':
            context['property_manager'] = self.request.user.propertymanager
        return context