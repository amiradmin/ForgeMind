from rest_framework.permissions import BasePermission


class BaseRBACPermission(BasePermission):
    """
    Base permission for RBAC.
    """

    permission_code = None

    def has_permission(self, request, view):
        raise NotImplementedError
