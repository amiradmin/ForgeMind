import pytest
from rest_framework.test import APIRequestFactory

from apps.identity.models import Permission, Role, User
from apps.identity.services.authorization import AuthorizationService
from shared.permissions.rbac import HasRBACPermission


class TestView:
    permission_code = "asset.view"


@pytest.mark.django_db
def test_rbac_permission_allows_user():

    user = User.objects.create_user(
        email="rbac@example.com",
        password="password123",
    )

    role = Role.objects.create(
        name="Viewer",
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

    request = APIRequestFactory().get("/api/v1/assets/")

    request.user = user

    permission_checker = HasRBACPermission()

    assert permission_checker.has_permission(
        request,
        TestView(),
    )
