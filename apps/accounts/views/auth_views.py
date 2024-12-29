from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from ..serializers.user_serializers import LoginSerializer, UserProfileSerializer, PropertyManagerSignupSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics

class LoginView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response('Successful login', UserProfileSerializer),
            401: 'Invalid credentials'
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        if not user:
            return Response(
                {'error': 'Invalid credentials'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': UserProfileSerializer(user).data
        })

class PropertyManagerSignupView(generics.CreateAPIView):
    serializer_class = PropertyManagerSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Property Manager created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)