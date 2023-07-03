from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_superuser or obj == request.user


class IsSellerAndOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return (
            request.user.is_seller and obj == request.user or request.user.is_superuser
        )


class IsSellerAndOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_seller
            and obj == request.user
            or request.user.is_superuser
        )
