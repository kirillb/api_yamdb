from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsCreating(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.method == 'POST'


class IsAuthor(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
