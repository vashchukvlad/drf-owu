from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from apps.auto_parks.models import AutoParkModel

from ..cars.serializers import CarSerializer
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, request, *args, **kwargs):
        auto_park = self.get_object()
        car_serializer = CarSerializer(data=request.data)
        car_serializer.is_valid(raise_exception=True)
        car_serializer.save(auto_park=auto_park)
        auto_park_serializer = AutoParkSerializer(auto_park)
        return Response(auto_park_serializer.data, status=HTTP_201_CREATED)