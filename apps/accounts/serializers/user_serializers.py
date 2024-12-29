from rest_framework import serializers
from ..models import User
from django.contrib.auth import get_user_model
from apps.properties.models import PropertyManager

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'phone_number', 'created_at']
        read_only_fields = ['created_at']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True, write_only=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'phone_number', 'created_at']
        read_only_fields = ['id', 'user_type', 'created_at']

class PropertyManagerSignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=150, min_length=1)
    password = serializers.CharField(write_only=True, min_length=1)
    company_name = serializers.CharField(required=True, max_length=100, min_length=1)
    address = serializers.CharField(required=True, min_length=1)

    class Meta:
        model = PropertyManager
        fields = ['username', 'company_name', 'address', 'password']

    def validate(self, attrs):
        # Check if a user with the same username already exists
        if User.objects.filter(username=attrs.get('username')).exists():
            raise serializers.ValidationError({"error": "User with this username already exists."})
        return attrs

    def create(self, validated_data):
        # Extract username and password
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        # Create the user
        user = User(
            username=username,  # Use the provided username
            user_type='property_manager'  # Assign user type
        )
        user.set_password(password)  # Hash the password
        user.save()

        # Create the PropertyManager instance without the username
        property_manager = PropertyManager.objects.create(user=user, **validated_data)
        return property_manager