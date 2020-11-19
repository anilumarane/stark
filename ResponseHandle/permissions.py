from rest_framework import permissions

from Account.models import MyUser
from ResponseHandle import exception_handler


class IsAdminAuth(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        if request.user.role_id.role_type=='admin':
            return request.user
        return not request.user