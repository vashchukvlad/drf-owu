from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView, get_object_or_404, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CarModel
from .serializers import CarSerializer, CarForReturnSerializer
from .filters import cars_filter


# class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         return super().list(self, *args, **kwargs)
#
#     def post(self, *args, **kwargs):
#         return super().create(self, *args, **kwargs)

class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        return cars_filter(query_params)


# class CarListCreateView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     def get(self, *args, **kwargs):
#         cars = CarModel.objects.all()
#         query_params = self.request.query_params
#
#         for k, v in query_params.items():
#             match k:
#                 case 'price__gt':
#                     cars = cars.filter(price__gt=v)
#                 case 'price__lt':
#                     cars = cars.filter(price__lt=v)
#                 case 'brand':
#                     cars = cars.filter(brand__exact=v)
#                 case _:
#                     raise ValidationError({'details': 'Invalid filter parameter'})
#         cars_serialized = CarForReturnSerializer(cars, many=True)
#         return Response(cars_serialized.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data # type: ignore
#         serialized = CarSerializer(data=data)
#
#         if not serialized.is_valid():
#             return Response(serialized.errors, status.HTTP_400_BAD_REQUEST)
#
#         serialized.save()
#         return Response(serialized.data, status.HTTP_201_CREATED)


class CarGetUpdateDeleteView(GenericAPIView):
    queryset = CarModel.objects.all()
    def get(self, *args, **kwargs):
        # pk = kwargs['pk']
        #
        # # better way
        # #car = get_object_or_404(CarModel, pk=pk)
        #
        # # try:
        # #     car = CarModel.objects.get(pk=pk)
        # # except CarModel.DoesNotExist:
        # #     return Response({'message': 'The car does not exist'}, status.HTTP_404_NOT_FOUND)

        car = self.get_object()
        
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        # pk = kwargs['pk']
        # data = self.request.data # type: ignore
        #
        # try:
        #     car = CarModel.objects.get(pk=pk)
        # except CarModel.DoesNotExist:
        #     return Response({'message': 'The car does not exist'}, status.HTTP_404_NOT_FOUND)

        car = self.get_object()
        
        serializer = CarSerializer(car, data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data # type: ignore

        # try:
        #     car = CarModel.objects.get(pk=pk)
        # except CarModel.DoesNotExist:
        #     return Response({'message': 'The car does not exist'}, status.HTTP_404_NOT_FOUND)

        car = self.get_object()
        
        serializer = CarSerializer(car, data=data, partial=True)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        # pk = kwargs['pk']
        #
        # try:
        #     car = CarModel.objects.get(pk=pk)
        #     car.delete()
        # except CarModel.DoesNotExist:
        #     return Response({'message': 'The car does not exist'}, status.HTTP_404_NOT_FOUND)

        self.get_object().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)