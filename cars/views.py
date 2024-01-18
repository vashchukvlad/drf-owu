from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CarModel
from .serializers import CarSerializer, CarForReturnSerializer


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        cars_serialized = CarForReturnSerializer(cars, many=True)
        return Response(cars_serialized.data, status.HTTP_200_OK)
    
    def post(self, *args, **kwargs):
        data = self.request.data # type: ignore
        serialized = CarSerializer(data=data)

        if not serialized.is_valid():
            return Response(serialized.errors, status.HTTP_400_BAD_REQUEST)
        
        serialized.save()
        return Response(serialized.data, status.HTTP_201_CREATED)


class CarGetUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response({'message': 'The car does not exist'}, status.HTTP_404_NOT_FOUND)
        
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data # type: ignore

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response({'message': 'The car does not exist'}, status.HTTP_404_NOT_FOUND)
        
        serializer = CarSerializer(car, data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data # type: ignore

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response({'message': 'The car does not exist'}, status.HTTP_404_NOT_FOUND)
        
        serializer = CarSerializer(car, data=data, partial=True)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            return Response({'message': 'The car does not exist'}, status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)
