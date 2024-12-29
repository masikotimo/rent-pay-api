from rest_framework import serializers
from ..models import Unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'property', 'unit_number', 'rent_amount', 'is_occupied']