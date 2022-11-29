from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django_extensions.db.models import TimeStampedModel

from helpers.enums import UserRole

ROLE_CHOICES = (
    (UserRole.GUEST.value, "Guest"),
    (UserRole.PARTICIPANT.value, "Participant"),
    (UserRole.CREATOR.value, "Creator"),
    (UserRole.ADMIN.value, "Admin"),
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra):
        if not username:
            raise ValueError("Username is required.")
        if not email:
            raise ValueError("Email is required.")
        user = self.model(username=username, email=self.normalize_email(email), **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra):
        extra.setdefault("is_superuser", True)
        extra.setdefault("is_staff", True)
        return self.create_user(
            username=username, email=email, password=password, **extra
        )


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(primary_key=True, max_length=255)
    username = models.CharField(max_length=120, unique=True, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "user"
