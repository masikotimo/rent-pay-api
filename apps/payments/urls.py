from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, PaymentReconciliationViewSet

router = DefaultRouter()
router.register('payments', PaymentViewSet)
router.register('reconciliations', PaymentReconciliationViewSet)

urlpatterns = router.urls