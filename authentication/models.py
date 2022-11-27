from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from helpers.models import BaseModel


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


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(primary_key=True, max_length=255)
    username = models.CharField(max_length=120, unique=True, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    quizzes = models.ManyToManyField("quizzes.Quiz")
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "user"

    @property
    def token(self):
        return ""
