from .user_serializers import UserSerializer, LoginSerializer, UserProfileSerializer
from .property_manager_serializers import PropertyManagerCreateSerializer, PropertyManagerDetailSerializer
from .tenant_serializers import TenantCreateSerializer, TenantDetailSerializer

__all__ = [
    'UserSerializer',
    'LoginSerializer',
    'UserProfileSerializer',
    'PropertyManagerCreateSerializer',
    'PropertyManagerDetailSerializer',
    'TenantCreateSerializer',
    'TenantDetailSerializer',
]