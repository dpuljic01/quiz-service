from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
        ]


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(required=False)
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    @staticmethod
    def validate_email(email):
        user_db = User.objects.get(email)
        if user_db:
            raise serializers.ValidationError(
                f"User with that email {email} already exists."
            )
        return email

    def validate(self, data):
        if not data.get("password") or not data.get("confirm_password"):
            raise serializers.ValidationError("Please enter a password and confirm it.")
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError("Passwords don't match.")
        return data


#
#
# class PasswordSerializer(serializers.Serializer):
#
