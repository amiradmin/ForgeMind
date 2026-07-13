from rest_framework.permissions import BasePermission

from apps.identity.services.authorization import AuthorizationService


class HasRBACPermission(BasePermission):
    """
    Generic RBAC permission checker.

    Usage:

        permission_code = "asset.view"
    """

    def has_permission(self, request, view):
        permission_code = getattr(
            view,
            "permission_code",
            None,
        )

        if permission_code is None:
            return False

        return AuthorizationService.user_has_permission(
            request.user,
            permission_code,
        )
