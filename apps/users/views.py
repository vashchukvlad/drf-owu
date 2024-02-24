from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from ..auto_parks.serializers import AutoParkSerializer
from .models import UserModel
from .serializer import UserSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserAddAutoParkView(GenericAPIView):
    queryset = UserModel.objects.all()

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        auto_park = request.data
        auto_park_serializer = AutoParkSerializer(data=auto_park)
        auto_park_serializer.is_valid(raise_exception=True)
        auto_park_serializer.save(user=user)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
