from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Property Management API",
        default_version='v1',
        description="API documentation for Property Management System",
        contact=openapi.Contact(email="support@propertymanagement.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Redirect root URL to Swagger UI
    path('', RedirectView.as_view(url='/swagger/', permanent=False), name='index'),
    
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.accounts.urls')),
    path('api/v1/', include('apps.properties.urls')),
    path('api/v1/', include('apps.payments.urls')),
    path('api/v1/', include('apps.ussd.urls')),
    
    # Swagger UI and ReDoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)