import factory
from django.utils import timezone

from apps.assets.tests.factories import AssetFactory
from apps.identity.models import User
from apps.telemetry.models.enums import (
    IndustrialEventSeverity,
    IndustrialEventStatus,
    IndustrialEventType,
    TelemetryQuality,
)
from apps.telemetry.models.industrial_event import IndustrialEvent
from apps.telemetry.models.telemetry import Telemetry


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(
        lambda n: f"telemetry-user-{n}@example.com",
    )

    password = factory.PostGenerationMethodCall(
        "set_password",
        "test-password",
    )

    first_name = "Test"
    last_name = "User"
    is_active = True


class IndustrialEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IndustrialEvent

    asset = factory.SubFactory(AssetFactory)

    event_type = IndustrialEventType.ALARM

    severity = IndustrialEventSeverity.HIGH

    status = IndustrialEventStatus.OPEN

    title = factory.Sequence(
        lambda n: f"Industrial Event {n}",
    )

    description = "Test industrial event description."

    occurred_at = factory.LazyFunction(
        timezone.now,
    )

    acknowledged_at = None

    resolved_at = None

    acknowledged_by = None

    resolved_by = None

    metadata = factory.LazyFunction(
        lambda: {
            "source": "test",
            "sensor_id": "sensor-001",
        },
    )


class TelemetryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Telemetry

    asset = factory.SubFactory(AssetFactory)

    metric = factory.Sequence(
        lambda n: f"temperature_{n}",
    )

    value = factory.Faker(
        "pyfloat",
        left_digits=2,
        right_digits=10,
        positive=True,
    )

    unit = "°C"

    quality = TelemetryQuality.GOOD

    recorded_at = factory.LazyFunction(
        timezone.now,
    )

    metadata = factory.LazyFunction(
        lambda: {
            "source": "test",
            "sensor_id": "sensor-001",
        },
    )
