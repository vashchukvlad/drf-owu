from django.urls import path

from .views import UserAddAutoParkView, UserGetUpdateDeleteView, UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('/<int:pk>', UserGetUpdateDeleteView.as_view(), name='user-get-update-delete'),
    path('/<int:pk>/auto_park', UserAddAutoParkView.as_view(), name='user-add-auto-park'),
]
