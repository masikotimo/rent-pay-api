from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,  TenantViewSet,
    LoginView, 
)
from apps.accounts.views.property_manager_views import PropertyManagerViewSet
from apps.accounts.views.auth_views import PropertyManagerSignupView


router = DefaultRouter()
router.register('users', UserViewSet)
# router.register('property-managers', PropertyManagerViewSet)
router.register('tenants', TenantViewSet)

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('api/v1/auth/signup/', PropertyManagerSignupView.as_view(), name='signup'),
    path('', include(router.urls)),
]