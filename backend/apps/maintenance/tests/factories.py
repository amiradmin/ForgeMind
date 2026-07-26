import factory

from apps.assets.tests.factories import AssetFactory
from apps.identity.tests.factories import UserFactory
from apps.maintenance.models import (
    MaintenancePlan,
    MaintenanceRequest,
    WorkOrder,
)


class MaintenancePlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MaintenancePlan

    asset = factory.SubFactory(AssetFactory)
    name = factory.Sequence(lambda n: f"Maintenance Plan {n}")
    maintenance_type = "preventive"
    frequency = 30
    frequency_unit = "days"
    start_date = factory.Faker("date")


class MaintenanceRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MaintenanceRequest

    asset = factory.SubFactory(AssetFactory)
    title = factory.Sequence(lambda n: f"Maintenance Request {n}")
    maintenance_type = "corrective"
    requested_by = factory.SubFactory(UserFactory)


class WorkOrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WorkOrder

    asset = factory.SubFactory(AssetFactory)
    title = factory.Sequence(lambda n: f"Work Order {n}")
    maintenance_type = "corrective"
    assigned_to = factory.SubFactory(UserFactory)
