import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.identity.models import Permission, Role, User
from apps.identity.services.authorization import AuthorizationService


@pytest.fixture
def authenticated_client(db):
    user = User.objects.create_user(
        email="user@test.com",
        password="password123",
    )

    role = Role.objects.create(
        name="Tester",
    )

    permissions = [
        "organization.view",
        "organization.create",
        "organization.update",
        "organization.delete",
        "plant.view",
        "plant.create",
        "plant.update",
        "plant.delete",
        "area.view",
        "area.create",
        "area.update",
        "area.delete",
        "asset.view",
        "asset.create",
        "asset.update",
        "asset.delete",
    ]

    for code in permissions:
        permission, _ = Permission.objects.get_or_create(
            code=code,
            defaults={
                "name": code.replace(".", " ").title(),
                "description": "",
            },
        )

        AuthorizationService.assign_permission(
            role,
            permission,
        )

    AuthorizationService.assign_role(
        user,
        role,
    )

    client = APIClient()

    refresh = RefreshToken.for_user(user)

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}",
    )

    return client
