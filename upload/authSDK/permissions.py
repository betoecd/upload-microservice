from .authentication import get_permission_data
from rest_framework.permissions import BasePermission


class LoginAuthMicroservice(BasePermission):
    """Authentication microservice permission"""

    def has_permission(self, request, view):
        permission_data = get_permission_data(request, "/ping")
        return permission_data
