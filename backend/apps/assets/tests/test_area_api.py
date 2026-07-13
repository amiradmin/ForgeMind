import pytest
from rest_framework.test import APIClient

from apps.assets.models import Area
from apps.assets.tests.factories import AreaFactory, OrganizationFactory, PlantFactory


@pytest.mark.django_db
def test_authentication_required():

    client = APIClient()

    response = client.get("/api/v1/areas/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_list_areas(authenticated_client):

    organization = OrganizationFactory()

    plant = PlantFactory(organization=organization)

    AreaFactory(
        plant=plant,
        name="Production Area",
    )

    response = authenticated_client.get("/api/v1/areas/")

    assert response.status_code == 200
    assert response.data["count"] == 1


@pytest.mark.django_db
def test_create_area(authenticated_client):

    organization = OrganizationFactory()

    plant = PlantFactory(organization=organization)

    payload = {
        "plant": str(plant.id),
        "name": "Assembly Area",
        "code": "AREA001",
    }

    response = authenticated_client.post(
        "/api/v1/areas/",
        payload,
        format="json",
    )

    assert response.status_code == 201

    assert Area.objects.filter(code="AREA001").exists()
