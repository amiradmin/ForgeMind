from django.contrib.auth import get_user_model

from apps.identity.models.permission import Permission
from apps.identity.models.role import Role
from apps.identity.models.role_permission import RolePermission
from apps.identity.models.user_role import UserRole

User = get_user_model()


class AuthorizationService:
    """
    Service responsible for Role-Based Access Control (RBAC).
    """

    @staticmethod
    def assign_role(user: User, role: Role) -> UserRole:
        user_role, _ = UserRole.objects.get_or_create(
            user=user,
            role=role,
        )
        return user_role

    @staticmethod
    def remove_role(user: User, role: Role) -> None:
        UserRole.objects.filter(
            user=user,
            role=role,
        ).delete()

    @staticmethod
    def assign_permission(
        role: Role,
        permission: Permission,
    ) -> RolePermission:
        role_permission, _ = RolePermission.objects.get_or_create(
            role=role,
            permission=permission,
        )
        return role_permission

    @staticmethod
    def remove_permission(
        role: Role,
        permission: Permission,
    ) -> None:
        RolePermission.objects.filter(
            role=role,
            permission=permission,
        ).delete()

    @staticmethod
    def user_has_role(
        user: User,
        role_name: str,
    ) -> bool:
        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        return UserRole.objects.filter(
            user=user,
            role__name=role_name,
        ).exists()

    @staticmethod
    def user_has_permission(
        user: User,
        permission_code: str,
    ) -> bool:
        """
        Check whether the user has a permission through any assigned role.
        """

        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        return UserRole.objects.filter(
            user=user,
            role__role_permissions__permission__code=permission_code,
        ).exists()

    @staticmethod
    def get_user_roles(user: User):
        return Role.objects.filter(
            user_roles__user=user,
        )

    @staticmethod
    def get_user_permissions(user: User):
        if user.is_superuser:
            return Permission.objects.all()

        return Permission.objects.filter(
            role_permissions__role__user_roles__user=user,
        ).distinct()
