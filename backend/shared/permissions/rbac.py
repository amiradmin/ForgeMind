from rest_framework.permissions import BasePermission

from apps.identity.services.authorization import AuthorizationService


class HasRBACPermission(BasePermission):

    action_permissions = {
        "list": "view",
        "retrieve": "view",
        "create": "create",
        "update": "update",
        "partial_update": "update",
        "destroy": "delete",
    }

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        # 1. Explicit permission_code on the view
        permission_code = getattr(view, "permission_code", None)

        if permission_code:
            return AuthorizationService.user_has_permission(
                request.user,
                permission_code,
            )

        # 2. ViewSet action-based permissions
        action = getattr(view, "action", None)

        if action is None:
            return False

        permission_code = getattr(view, "action_permissions", {}).get(action)

        if permission_code is None:
            return False

        return AuthorizationService.user_has_permission(
            request.user,
            permission_code,
        )
