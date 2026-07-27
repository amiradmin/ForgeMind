import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.identity.models import Permission, Role, User
from apps.identity.services.authorization import AuthorizationService


@pytest.fixture
def authenticated_client(db):
    user = User.objects.create_user(
        email="maintenance-user@test.com",
        password="password123",
    )

    role = Role.objects.create(
        name="Maintenance Tester",
    )

    permissions = [
        "maintenance_plan.view",
        "maintenance_plan.create",
        "maintenance_plan.update",
        "maintenance_plan.delete",
        "maintenance_request.view",
        "maintenance_request.create",
        "maintenance_request.update",
        "maintenance_request.delete",
        "work_order.view",
        "work_order.create",
        "work_order.update",
        "work_order.delete",
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