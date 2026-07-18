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

    plant = PlantFactory(
        organization=organization,
    )

    area = AreaFactory(
        plant=plant,
    )

    AssetFactory(
        area=area,
        name="Pump A",
    )

    response = authenticated_client.get(
        "/api/v1/assets/",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1


@pytest.mark.django_db
def test_create_asset(authenticated_client):
    organization = OrganizationFactory()

    plant = PlantFactory(
        organization=organization,
    )

    area = AreaFactory(
        plant=plant,
    )

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
        "installation_date": "2026-01-10",
        "commissioned_at": "2026-01-15",
        "last_maintenance_at": "2026-06-01",
        "retired_at": None,
        "lifecycle_status": "operational",
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

    assert response.status_code == 201

    asset = Asset.objects.get(
        code="PUMP001",
    )

    assert asset.name == "Main Pump"
    assert asset.lifecycle_status == "operational"
    assert asset.metadata["power"] == "15KW"

    assert response.data["lifecycle_status"] == "operational"
    assert response.data["asset_type_name"] == "Pump"


@pytest.mark.django_db
def test_filter_assets_by_lifecycle_status(authenticated_client):
    organization = OrganizationFactory()

    plant = PlantFactory(
        organization=organization,
    )

    area = AreaFactory(
        plant=plant,
    )

    asset_type = AssetTypeFactory(
        name="Pump",
        code="pump",
    )

    AssetFactory(
        area=area,
        asset_type=asset_type,
        name="Operational Pump",
        lifecycle_status="operational",
    )

    AssetFactory(
        area=area,
        asset_type=asset_type,
        name="Maintenance Pump",
        lifecycle_status="maintenance",
    )

    response = authenticated_client.get(
        "/api/v1/assets/?lifecycle_status=operational",
    )

    assert response.status_code == 200

    assert response.data["count"] == 1

    assert response.data["results"][0]["lifecycle_status"] == "operational"
