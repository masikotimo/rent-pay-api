from rest_framework import serializers
from ..models import Property
from .unit_serializers import UnitSerializer

class PropertySerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)
    total_units = serializers.IntegerField(read_only=True)
    occupied_units = serializers.IntegerField(read_only=True)
    total_rent = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Property
        fields = ['id', 'name', 'address', 'property_manager', 'units',
                 'total_units', 'occupied_units', 'total_rent', 'created_at']