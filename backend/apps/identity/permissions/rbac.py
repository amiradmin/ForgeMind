from rest_framework.permissions import BasePermission

from apps.identity.services.authorization import AuthorizationService


class HasRBACPermission(BasePermission):
    """
    Generic RBAC permission checker.
    """

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        permission = None

        if hasattr(view, "action_permissions"):
            permission = view.action_permissions.get(view.action)

        if permission is None:
            return True

        return AuthorizationService.user_has_permission(
            request.user,
            permission,
        )
