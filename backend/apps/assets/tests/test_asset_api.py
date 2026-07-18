import pytest
from rest_framework.test import APIClient

from apps.assets.models import Asset
from apps.assets.tests.factories import (
    AreaFactory,
    AssetFactory,
    AssetTypeFactory,
    OrganizationFactory,
    PlantFactory,
)


@pytest.mark.django_db
def test_authentication_required():

    client = APIClient()

    response = client.get("/api/v1/assets/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_list_assets(authenticated_client):

    organization = OrganizationFactory()

    plant = PlantFactory(organization=organization)

    area = AreaFactory(plant=plant)

    AssetFactory(
        area=area,
        name="Pump A",
    )

    response = authenticated_client.get("/api/v1/assets/")

    assert response.status_code == 200
    assert response.data["count"] == 1


@pytest.mark.django_db
def test_create_asset(authenticated_client):

    organization = OrganizationFactory()

    plant = PlantFactory(organization=organization)

    area = AreaFactory(plant=plant)

    asset_type = AssetTypeFactory(
        name="Pump",
        code="pump",
    )

    payload = {
        "area": str(area.id),
        "name": "Main Pump",
        "code": "PUMP001",
        "asset_type": str(asset_type.id),
        "manufacturer": "Siemens",
        "model": "SIM-100",
        "serial_number": "SN-001",
        "metadata": {
            "power": "15KW",
            "pressure": "10bar",
        },
    }

    response = authenticated_client.post(
        "/api/v1/assets/",
        payload,
        format="json",
    )

    print(response.data)

    assert response.status_code == 201

    assert Asset.objects.filter(code="PUMP001").exists()
