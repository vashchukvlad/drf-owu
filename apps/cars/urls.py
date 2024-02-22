from django.urls import path

from .views import CarListCreateView, CarGetUpdateDeleteView


urlpatterns = [
    path('', CarListCreateView.as_view(), name='car-list-create'),
    path('/<int:pk>', CarGetUpdateDeleteView.as_view(), name='car-get-update-delete')
]
