from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import USSDSession, USSDLog
from apps.accounts.models import Tenant
from ..services.ussd_menu_service import USSDMenuService
from django.http import HttpResponse

class USSDCallbackView(APIView):
    permission_classes = []  # Allow unauthenticated access for USSD callbacks

    def post(self, request):
        session_id = request.data.get('sessionId')
        phone_number = request.data.get('phoneNumber')
        text = request.data.get('text', '')

        # Get or create session
        session, created = USSDSession.objects.get_or_create(
            session_id=session_id,
            defaults={'phone_number': phone_number, 'current_menu': 'MAIN'}  # Set default current_menu
        )

        # Log the USSD input
        USSDLog.objects.create(
            session=session,
            input=text,
            response=''  # Will be updated after processing
        )

        # Process USSD menu
        menu_service = USSDMenuService(session, text)
        response = menu_service.process()  # This should return a properly formatted response

        # Strip any extra whitespace
        response = response.strip()
        # Update the log with the response
        log_entry = USSDLog.objects.filter(session=session).order_by('-created_at').first()
        if log_entry:
            log_entry.response = response
            log_entry.save()

        return HttpResponse(response)