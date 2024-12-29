from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from ..models import PropertyManager, User
from .user_serializers import UserSerializer

class PropertyManagerCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)

    class Meta:
        model = PropertyManager
        fields = ['username', 'email', 'password', 'phone_number', 
                 'company_name', 'address']

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user_data = {
            'username': validated_data.pop('username'),
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password'),
            'phone_number': validated_data.pop('phone_number'),
            'user_type': 'property_manager'
        }
        
        user = User.objects.create_user(**user_data)
        property_manager = PropertyManager.objects.create(user=user, **validated_data)
        
        return property_manager

class PropertyManagerDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    total_properties = serializers.IntegerField(read_only=True)
    total_tenants = serializers.IntegerField(read_only=True)

    class Meta:
        model = PropertyManager
        fields = ['id', 'user', 'company_name', 'address', 'is_active', 
                 'total_properties', 'total_tenants']