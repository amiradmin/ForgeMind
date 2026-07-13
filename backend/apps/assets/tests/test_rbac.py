import pytest
from rest_framework import status
from rest_framework.test import APIClient

from apps.identity.models import User


@pytest.mark.django_db
def test_user_without_permission_gets_403():
    user = User.objects.create_user(
        email="user@test.com",
        password="password123",
    )

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/v1/organizations/")

    assert response.status_code == status.HTTP_403_FORBIDDEN
