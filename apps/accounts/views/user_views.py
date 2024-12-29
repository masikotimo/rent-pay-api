from rest_framework import viewsets, permissions
from ..models import User
from ..serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        if self.request.user.user_type == 'property_manager':
            return User.objects.filter(tenant__property_manager=self.request.user.propertymanager)
        return super().get_queryset()