from datetime import date

import pytest

from apps.assets.tests.factories import AssetFactory
from apps.identity.models import User
from apps.maintenance.models import (
    MaintenanceFrequencyUnit,
    MaintenancePlan,
    MaintenancePriority,
    MaintenanceRequest,
    MaintenanceRequestStatus,
    MaintenanceType,
    WorkOrder,
    WorkOrderStatus,
)


@pytest.mark.django_db
class TestMaintenancePlan:
    def test_create_maintenance_plan(self):
        asset = AssetFactory()

        plan = MaintenancePlan.objects.create(
            asset=asset,
            name="Monthly Pump Inspection",
            description="Monthly inspection of pump equipment.",
            maintenance_type=MaintenanceType.PREVENTIVE,
            frequency=1,
            frequency_unit=MaintenanceFrequencyUnit.MONTHS,
            start_date=date(2026, 7, 1),
        )

        assert plan.pk is not None
        assert plan.asset == asset
        assert plan.name == "Monthly Pump Inspection"
        assert plan.maintenance_type == MaintenanceType.PREVENTIVE
        assert plan.frequency == 1
        assert plan.frequency_unit == MaintenanceFrequencyUnit.MONTHS

    def test_maintenance_plan_string_representation(self):
        asset = AssetFactory()

        plan = MaintenancePlan.objects.create(
            asset=asset,
            name="Pump Inspection",
            maintenance_type=MaintenanceType.PREVENTIVE,
            frequency=30,
            frequency_unit=MaintenanceFrequencyUnit.DAYS,
            start_date=date(2026, 7, 1),
        )

        assert str(plan) == "Pump Inspection"


@pytest.mark.django_db
class TestMaintenanceRequest:
    def test_create_maintenance_request(self):
        asset = AssetFactory()

        user = User.objects.create_user(
            email="technician@example.com",
            password="test-password",
        )

        request = MaintenanceRequest.objects.create(
            asset=asset,
            title="Pump Failure",
            description="Pump is making abnormal noise.",
            maintenance_type=MaintenanceType.CORRECTIVE,
            priority=MaintenancePriority.HIGH,
            requested_by=user,
        )

        assert request.pk is not None
        assert request.asset == asset
        assert request.requested_by == user
        assert request.title == "Pump Failure"
        assert request.maintenance_type == MaintenanceType.CORRECTIVE
        assert request.priority == MaintenancePriority.HIGH
        assert request.status == MaintenanceRequestStatus.OPEN

    def test_maintenance_request_can_be_linked_to_plan(self):
        asset = AssetFactory()

        plan = MaintenancePlan.objects.create(
            asset=asset,
            name="Preventive Plan",
            maintenance_type=MaintenanceType.PREVENTIVE,
            frequency=30,
            frequency_unit=MaintenanceFrequencyUnit.DAYS,
            start_date=date(2026, 7, 1),
        )

        request = MaintenanceRequest.objects.create(
            asset=asset,
            maintenance_plan=plan,
            title="Scheduled Maintenance",
            maintenance_type=MaintenanceType.PREVENTIVE,
        )

        assert request.maintenance_plan == plan

    def test_maintenance_request_string_representation(self):
        asset = AssetFactory()

        request = MaintenanceRequest.objects.create(
            asset=asset,
            title="Pump Failure",
            maintenance_type=MaintenanceType.CORRECTIVE,
        )

        assert str(request) == "Pump Failure"


@pytest.mark.django_db
class TestWorkOrder:
    def test_create_work_order(self):
        asset = AssetFactory()

        user = User.objects.create_user(
            email="technician@example.com",
            password="test-password",
        )

        work_order = WorkOrder.objects.create(
            asset=asset,
            title="Repair Pump",
            description="Replace damaged pump component.",
            maintenance_type=MaintenanceType.CORRECTIVE,
            priority=MaintenancePriority.CRITICAL,
            assigned_to=user,
        )

        assert work_order.pk is not None
        assert work_order.asset == asset
        assert work_order.assigned_to == user
        assert work_order.title == "Repair Pump"
        assert work_order.maintenance_type == MaintenanceType.CORRECTIVE
        assert work_order.priority == MaintenancePriority.CRITICAL
        assert work_order.status == WorkOrderStatus.OPEN

    def test_work_order_can_be_linked_to_maintenance_request(self):
        asset = AssetFactory()

        request = MaintenanceRequest.objects.create(
            asset=asset,
            title="Motor Failure",
            maintenance_type=MaintenanceType.CORRECTIVE,
        )

        work_order = WorkOrder.objects.create(
            asset=asset,
            maintenance_request=request,
            title="Repair Motor",
            maintenance_type=MaintenanceType.CORRECTIVE,
        )

        assert work_order.maintenance_request == request

    def test_work_order_string_representation(self):
        asset = AssetFactory()

        work_order = WorkOrder.objects.create(
            asset=asset,
            title="Repair Pump",
            maintenance_type=MaintenanceType.CORRECTIVE,
        )

        assert str(work_order) == "Repair Pump"