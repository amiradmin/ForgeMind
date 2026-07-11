import pytest
from rest_framework.test import APIClient

from apps.assets.tests.factories import OrganizationFactory


@pytest.mark.django_db
def test_authentication_required():

    client = APIClient()

    response = client.get(
        "/api/v1/organizations/"
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_list_organizations(authenticated_client):

    OrganizationFactory.create(
        name="Test Organization",
        code="TEST001",
    )

    response = authenticated_client.get(
        "/api/v1/organizations/"
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["name"] == "Test Organization"