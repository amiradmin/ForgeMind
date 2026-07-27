import factory
from django.contrib.auth import get_user_model

from apps.assets.tests.factories import AssetFactory
from apps.maintenance.models import (
    MaintenancePlan,
    MaintenanceRequest,
    WorkOrder,
)

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(
        lambda obj: f"{obj.username}@example.com",
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
