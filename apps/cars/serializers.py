from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price', 'created_at', 'updated_at')

    def validate_brand(self, value):
        if value == 'RIO':
            raise ValidationError({'details': 'RIO is not allowed'})
        return value


class CarForReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year')
