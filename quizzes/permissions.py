from rest_framework import permissions
from rest_framework.permissions import BasePermission

from helpers.enums import UserRole


class QuizPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if hasattr(request.user, "owner"):
            quiz_id_list = request.user.get_quizzes().values_list("id", flat=True)
            return obj.id in quiz_id_list
        return False


class IsSuperuserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return hasattr(request.user, "owner")


class IsParticipantPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.role == UserRole.PARTICIPANT


class IsCreatorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.role == UserRole.CREATOR
