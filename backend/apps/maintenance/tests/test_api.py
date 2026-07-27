import pytest
from rest_framework.test import APIClient

from apps.assets.tests.factories import AssetFactory
from apps.maintenance.models import (
    MaintenancePlan,
    MaintenanceRequest,
    WorkOrder,
)
from apps.maintenance.tests.factories import (
    MaintenancePlanFactory,
    MaintenanceRequestFactory,
    WorkOrderFactory,
)

# =============================================================================
# Maintenance Plan API Tests
# =============================================================================


@pytest.mark.django_db
def test_maintenance_plan_authentication_required():
    client = APIClient()

    response = client.get(
        "/api/v1/maintenance-plans/",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_list_maintenance_plans(authenticated_client):
    asset = AssetFactory()

    MaintenancePlanFactory(
        asset=asset,
        name="Monthly Pump Maintenance",
    )

    response = authenticated_client.get(
        "/api/v1/maintenance-plans/",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["name"] == ("Monthly Pump Maintenance")


@pytest.mark.django_db
def test_create_maintenance_plan(authenticated_client):
    asset = AssetFactory()

    payload = {
        "asset": str(asset.id),
        "name": "Monthly Pump Maintenance",
        "description": "Monthly preventive maintenance",
        "maintenance_type": "preventive",
        "frequency": 1,
        "frequency_unit": "months",
        "start_date": "2026-07-01",
    }

    response = authenticated_client.post(
        "/api/v1/maintenance-plans/",
        payload,
        format="json",
    )

    assert response.status_code == 201

    plan = MaintenancePlan.objects.get(
        name="Monthly Pump Maintenance",
    )

    assert plan.asset == asset
    assert plan.maintenance_type == "preventive"
    assert plan.frequency == 1
    assert plan.frequency_unit == "months"
    assert plan.next_due_date is not None

    assert response.data["name"] == "Monthly Pump Maintenance"
    assert response.data["next_due_date"] is not None


@pytest.mark.django_db
def test_filter_maintenance_plans_by_asset(authenticated_client):
    asset = AssetFactory()

    MaintenancePlanFactory(
        asset=asset,
        name="Pump Maintenance",
    )

    other_asset = AssetFactory()

    MaintenancePlanFactory(
        asset=other_asset,
        name="Other Asset Maintenance",
    )

    response = authenticated_client.get(
        f"/api/v1/maintenance-plans/?asset={asset.id}",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["name"] == ("Pump Maintenance")


@pytest.mark.django_db
def test_search_maintenance_plans(authenticated_client):
    asset = AssetFactory(
        name="Main Cooling Pump",
    )

    MaintenancePlanFactory(
        asset=asset,
        name="Monthly Pump Maintenance",
        description="Preventive maintenance for the cooling pump",
    )

    MaintenancePlanFactory(
        name="Generator Maintenance",
        description="Generator inspection",
    )

    response = authenticated_client.get(
        "/api/v1/maintenance-plans/?search=cooling",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["name"] == ("Monthly Pump Maintenance")


@pytest.mark.django_db
def test_order_maintenance_plans(authenticated_client):
    MaintenancePlanFactory(
        name="Zebra Maintenance",
    )

    MaintenancePlanFactory(
        name="Alpha Maintenance",
    )

    response = authenticated_client.get(
        "/api/v1/maintenance-plans/?ordering=name",
    )

    assert response.status_code == 200
    assert response.data["count"] == 2
    assert response.data["results"][0]["name"] == ("Alpha Maintenance")
    assert response.data["results"][1]["name"] == ("Zebra Maintenance")


@pytest.mark.django_db
def test_paginate_maintenance_plans(authenticated_client):
    for index in range(25):
        MaintenancePlanFactory(
            name=f"Maintenance Plan {index:02d}",
        )

    response = authenticated_client.get(
        "/api/v1/maintenance-plans/?page=2",
    )

    assert response.status_code == 200
    assert response.data["count"] == 25
    assert len(response.data["results"]) == 5
    assert response.data["previous"] is not None


# =============================================================================
# Maintenance Request API Tests
# =============================================================================


@pytest.mark.django_db
def test_maintenance_request_authentication_required():
    client = APIClient()

    response = client.get(
        "/api/v1/maintenance-requests/",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_list_maintenance_requests(authenticated_client):
    asset = AssetFactory()

    MaintenanceRequestFactory(
        asset=asset,
        title="Pump Failure",
    )

    response = authenticated_client.get(
        "/api/v1/maintenance-requests/",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["title"] == ("Pump Failure")


@pytest.mark.django_db
def test_create_maintenance_request(authenticated_client):
    asset = AssetFactory()

    payload = {
        "asset": str(asset.id),
        "title": "Pump Failure",
        "description": "Main pump is not working",
        "maintenance_type": "corrective",
        "priority": "high",
    }

    response = authenticated_client.post(
        "/api/v1/maintenance-requests/",
        payload,
        format="json",
    )

    assert response.status_code == 201

    maintenance_request = MaintenanceRequest.objects.get(
        title="Pump Failure",
    )

    assert maintenance_request.asset == asset
    assert maintenance_request.maintenance_type == "corrective"
    assert maintenance_request.priority == "high"
    assert maintenance_request.requested_by is not None

    assert response.data["title"] == "Pump Failure"
    assert response.data["priority"] == "high"


@pytest.mark.django_db
def test_filter_maintenance_requests_by_status(authenticated_client):
    MaintenanceRequestFactory(
        title="Open Pump Failure",
        status="open",
    )

    MaintenanceRequestFactory(
        title="Resolved Pump Failure",
        status="resolved",
    )

    response = authenticated_client.get(
        "/api/v1/maintenance-requests/?status=open",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["title"] == ("Open Pump Failure")


@pytest.mark.django_db
def test_search_maintenance_requests(authenticated_client):
    asset = AssetFactory(
        name="Main Cooling Pump",
    )

    MaintenanceRequestFactory(
        asset=asset,
        title="Pump Failure",
        description="Cooling system failure",
    )

    MaintenanceRequestFactory(
        title="Generator Failure",
        description="Generator is not working",
    )

    response = authenticated_client.get(
        "/api/v1/maintenance-requests/?search=cooling",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["title"] == ("Pump Failure")


@pytest.mark.django_db
def test_order_maintenance_requests(authenticated_client):
    MaintenanceRequestFactory(
        title="Zebra Failure",
    )

    MaintenanceRequestFactory(
        title="Alpha Failure",
    )

    response = authenticated_client.get(
        "/api/v1/maintenance-requests/?ordering=title",
    )

    assert response.status_code == 200
    assert response.data["count"] == 2
    assert response.data["results"][0]["title"] == ("Alpha Failure")
    assert response.data["results"][1]["title"] == ("Zebra Failure")


@pytest.mark.django_db
def test_paginate_maintenance_requests(authenticated_client):
    for index in range(25):
        MaintenanceRequestFactory(
            title=f"Maintenance Request {index:02d}",
        )

    response = authenticated_client.get(
        "/api/v1/maintenance-requests/?page=2",
    )

    assert response.status_code == 200
    assert response.data["count"] == 25
    assert len(response.data["results"]) == 5
    assert response.data["previous"] is not None


# =============================================================================
# Work Order API Tests
# =============================================================================


@pytest.mark.django_db
def test_work_order_authentication_required():
    client = APIClient()

    response = client.get(
        "/api/v1/work-orders/",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_list_work_orders(authenticated_client):
    asset = AssetFactory()

    WorkOrderFactory(
        asset=asset,
        title="Repair Main Pump",
    )

    response = authenticated_client.get(
        "/api/v1/work-orders/",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["title"] == ("Repair Main Pump")


@pytest.mark.django_db
def test_create_work_order(authenticated_client):
    asset = AssetFactory()

    payload = {
        "asset": str(asset.id),
        "title": "Repair Main Pump",
        "description": "Repair the main cooling pump",
        "maintenance_type": "corrective",
        "priority": "high",
        "status": "open",
        "scheduled_start": "2026-07-20T08:00:00Z",
        "scheduled_end": "2026-07-20T12:00:00Z",
        "completion_notes": "",
    }

    response = authenticated_client.post(
        "/api/v1/work-orders/",
        payload,
        format="json",
    )

    assert response.status_code == 201

    work_order = WorkOrder.objects.get(
        title="Repair Main Pump",
    )

    assert work_order.asset == asset
    assert work_order.maintenance_type == "corrective"
    assert work_order.priority == "high"
    assert work_order.status == "open"

    assert response.data["title"] == "Repair Main Pump"
    assert response.data["priority"] == "high"


@pytest.mark.django_db
def test_filter_work_orders_by_status(authenticated_client):
    WorkOrderFactory(
        title="Open Pump Repair",
        status="open",
    )

    WorkOrderFactory(
        title="Completed Pump Repair",
        status="completed",
    )

    response = authenticated_client.get(
        "/api/v1/work-orders/?status=open",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["title"] == ("Open Pump Repair")


@pytest.mark.django_db
def test_search_work_orders(authenticated_client):
    asset = AssetFactory(
        name="Main Cooling Pump",
    )

    WorkOrderFactory(
        asset=asset,
        title="Repair Pump",
        description="Repair cooling system",
    )

    WorkOrderFactory(
        title="Repair Generator",
        description="Repair generator system",
    )

    response = authenticated_client.get(
        "/api/v1/work-orders/?search=cooling",
    )

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["title"] == ("Repair Pump")


@pytest.mark.django_db
def test_order_work_orders(authenticated_client):
    WorkOrderFactory(
        title="Zebra Repair",
    )

    WorkOrderFactory(
        title="Alpha Repair",
    )

    response = authenticated_client.get(
        "/api/v1/work-orders/?ordering=title",
    )

    assert response.status_code == 200
    assert response.data["count"] == 2
    assert response.data["results"][0]["title"] == ("Alpha Repair")
    assert response.data["results"][1]["title"] == ("Zebra Repair")


@pytest.mark.django_db
def test_paginate_work_orders(authenticated_client):
    for index in range(25):
        WorkOrderFactory(
            title=f"Work Order {index:02d}",
        )

    response = authenticated_client.get(
        "/api/v1/work-orders/?page=2",
    )

    assert response.status_code == 200
    assert response.data["count"] == 25
    assert len(response.data["results"]) == 5
    assert response.data["previous"] is not None
