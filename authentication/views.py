from rest_framework import generics

from authentication.models import User
from authentication.serializers import UserSerializer
from quizzes.permissions import IsSuperuserPermission


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperuserPermission]

    def perform_create(self, serializer):
        serializer.save()


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     @action(detail=True, methods=["post"], permission_classes=[AllowAny])
#     def register(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         model_serializer = UserSerializer(data=serializer.data)
#         model_serializer.is_valid(raise_exception=True)
#         model_serializer.save()
#
#         return Response(model_serializer.data)
