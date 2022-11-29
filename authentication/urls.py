from django.urls import path

from authentication.views import UserListCreateAPIView

urlpatterns = [path("", UserListCreateAPIView.as_view(), name="user-list-create")]
