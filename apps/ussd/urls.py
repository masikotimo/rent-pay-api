from django.urls import path
from .views import USSDCallbackView

urlpatterns = [
    path('ussd/callback/', USSDCallbackView.as_view(), name='ussd-callback'),
]