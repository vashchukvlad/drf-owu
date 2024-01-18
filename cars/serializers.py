from rest_framework import serializers

from .models import CarModel

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    number_of_seats = serializers.IntegerField()
    body_type = serializers.CharField()
    engine_volume = serializers.FloatField()

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data: dict):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance
    

class CarForReturnSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    brand = serializers.CharField(max_length=50)
    year = serializers.IntegerField()