import pytest
from rest_framework.test import APIClient

from apps.assets.models import Plant
from apps.assets.tests.factories import (
    OrganizationFactory,
    PlantFactory,
)
from apps.identity.models import User


@pytest.fixture
def authenticated_client(db):
    user = User.objects.create_user(
        username="testuser",
        password="password123",
    )

    client = APIClient()
    client.force_authenticate(user=user)

    return client


@pytest.mark.django_db
def test_authentication_required():
    client = APIClient()

    response = client.get("/api/v1/plants/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_list_plants(authenticated_client):
    organization = OrganizationFactory()

    PlantFactory(
        organization=organization,
        name="Factory Plant",
    )

    response = authenticated_client.get("/api/v1/plants/")

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["name"] == "Factory Plant"


@pytest.mark.django_db
def test_create_plant(authenticated_client):
    organization = OrganizationFactory()

    payload = {
        "organization": str(organization.id),
        "name": "New Plant",
        "code": "PLANT001",
    }

    response = authenticated_client.post(
        "/api/v1/plants/",
        payload,
        format="json",
    )

    assert response.status_code == 201
    assert Plant.objects.filter(code="PLANT001").exists()


@pytest.mark.django_db
def test_filter_plants(authenticated_client):
    organization = OrganizationFactory()

    PlantFactory(
        organization=organization,
        name="Tehran Plant",
    )

    response = authenticated_client.get("/api/v1/plants/?search=Tehran")

    assert response.status_code == 200
    assert response.data["count"] == 1
