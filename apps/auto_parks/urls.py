from django.urls import path

from .views import AutoParkAddListCarView, AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/cars', AutoParkAddListCarView.as_view(), name='auto_park_add_car'),
]
