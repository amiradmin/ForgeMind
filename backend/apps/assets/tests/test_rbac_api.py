import pytest
from rest_framework import status
from rest_framework.test import APIClient

from apps.identity.models import Permission, Role, RolePermission, User, UserRole


@pytest.mark.django_db
class TestAssetRBACAPI:
    """
    Test RBAC authorization on Asset API.
    """

    @pytest.fixture
    def client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return User.objects.create_user(
            email="user@test.com",
            password="password123",
        )

    @pytest.fixture
    def superuser(self):
        return User.objects.create_superuser(
            email="admin@test.com",
            password="password123",
        )

    @pytest.fixture
    def view_asset_permission(self):
        """
        Permission required to view assets.
        """

        return Permission.objects.create(
            code="asset.view",
            name="View Asset",
            description="Can view assets",
        )

    @pytest.fixture
    def asset_role(
        self,
        view_asset_permission,
    ):
        """
        Role with asset.view permission.
        """

        role = Role.objects.create(
            name="Asset Viewer",
            description="Can view assets",
        )

        RolePermission.objects.create(
            role=role,
            permission=view_asset_permission,
        )

        return role

    def test_user_without_permission_cannot_access_assets(
        self,
        client,
        user,
    ):
        """
        User without RBAC permission should get 403.
        """

        client.force_authenticate(
            user=user,
        )

        response = client.get(
            "/api/v1/assets/",
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_user_with_permission_can_access_assets(
        self,
        client,
        user,
        asset_role,
    ):
        """
        User with asset.view permission should get 200.
        """

        UserRole.objects.create(
            user=user,
            role=asset_role,
        )

        client.force_authenticate(
            user=user,
        )

        response = client.get(
            "/api/v1/assets/",
        )

        assert response.status_code == status.HTTP_200_OK

    def test_superuser_can_access_assets(
        self,
        client,
        superuser,
    ):
        """
        Superusers bypass RBAC.
        """

        client.force_authenticate(
            user=superuser,
        )

        response = client.get(
            "/api/v1/assets/",
        )

        assert response.status_code == status.HTTP_200_OK
