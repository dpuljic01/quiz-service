from django.http import JsonResponse
from rest_framework.decorators import api_view

from authentication.models import User
from authentication.serializers import UserSerializer


@api_view(["POST"])
def login(request, *args, **kwargs):
    instance = User.objects.filter(request.data["id"])
    response = UserSerializer(instance)
    return JsonResponse(response.data)
