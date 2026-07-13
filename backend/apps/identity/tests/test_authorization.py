import pytest

from apps.identity.models import Permission, Role, User
from apps.identity.services.authorization import AuthorizationService


@pytest.mark.django_db
def test_user_has_permission():

    user = User.objects.create_user(
        email="test@example.com",
        password="password123",
    )

    role = Role.objects.create(
        name="Manager",
    )

    permission = Permission.objects.create(
        code="asset.view",
        description="View assets",
    )

    AuthorizationService.assign_role(
        user,
        role,
    )

    AuthorizationService.assign_permission(
        role,
        permission,
    )

    assert AuthorizationService.user_has_permission(
        user,
        "asset.view",
    )
