from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import USSDSession, USSDLog
from apps.accounts.models import Tenant
from ..services.ussd_menu_service import USSDMenuService

class USSDCallbackView(APIView):
    permission_classes = []  # Allow unauthenticated access for USSD callbacks

    def post(self, request):
        session_id = request.data.get('sessionId')
        phone_number = request.data.get('phoneNumber')
        text = request.data.get('text', '')

        # Get or create session
        session, _ = USSDSession.objects.get_or_create(
            session_id=session_id,
            defaults={'phone_number': phone_number}
        )

        # Log the USSD input
        USSDLog.objects.create(
            session=session,
            input=text,
            response=''  # Will be updated after processing
        )

        # Process USSD menu
        menu_service = USSDMenuService(session, text)
        response = menu_service.process()

        # Update the log with the response
        USSDLog.objects.filter(
            session=session
        ).order_by('-created_at').first().update(response=response)

        return Response({'response': response}, status=status.HTTP_200_OK)