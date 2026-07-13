import pytest
from rest_framework import status
from rest_framework.test import APIClient

from apps.identity.models import Permission, Role, RolePermission, User, UserRole


@pytest.mark.django_db
class TestAreaRBACAPI:

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
    def area_permission(self):
        return Permission.objects.create(
            code="area.view",
            name="View Area",
            description="Can view areas",
        )

    @pytest.fixture
    def area_role(
        self,
        area_permission,
    ):
        role = Role.objects.create(
            name="Area Viewer",
        )

        RolePermission.objects.create(
            role=role,
            permission=area_permission,
        )

        return role

    def test_user_without_permission_cannot_access_areas(
        self,
        client,
        user,
    ):
        client.force_authenticate(user=user)

        response = client.get(
            "/api/v1/areas/",
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_user_with_permission_can_access_areas(
        self,
        client,
        user,
        area_role,
    ):
        UserRole.objects.create(
            user=user,
            role=area_role,
        )

        client.force_authenticate(user=user)

        response = client.get(
            "/api/v1/areas/",
        )

        assert response.status_code == status.HTTP_200_OK

    def test_superuser_can_access_areas(
        self,
        client,
        superuser,
    ):
        client.force_authenticate(user=superuser)

        response = client.get(
            "/api/v1/areas/",
        )

        assert response.status_code == status.HTTP_200_OK
