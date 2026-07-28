from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.telemetry.models.enums import (
    IndustrialEventSeverity,
    IndustrialEventStatus,
    IndustrialEventType,
    TelemetryQuality,
)
from apps.telemetry.models.industrial_event import IndustrialEvent
from apps.telemetry.models.telemetry import Telemetry
from apps.telemetry.tests.factories import (
    IndustrialEventFactory,
    TelemetryFactory,
)


class TestIndustrialEventModel(TestCase):
    def test_create_industrial_event(self):
        event = IndustrialEventFactory()

        self.assertIsNotNone(event.id)
        self.assertIsNotNone(event.asset)
        self.assertEqual(
            event.event_type,
            IndustrialEventType.ALARM,
        )
        self.assertEqual(
            event.severity,
            IndustrialEventSeverity.HIGH,
        )
        self.assertEqual(
            event.status,
            IndustrialEventStatus.OPEN,
        )

    def test_industrial_event_string_representation(self):
        event = IndustrialEventFactory(
            title="High Temperature Alarm",
        )

        expected = f"{event.asset} - High Temperature Alarm"

        self.assertEqual(
            str(event),
            expected,
        )

    def test_industrial_event_default_status_is_open(self):
        event = IndustrialEventFactory(
            status=IndustrialEventStatus.OPEN,
        )

        self.assertEqual(
            event.status,
            IndustrialEventStatus.OPEN,
        )

    def test_industrial_event_default_severity(self):
        event = IndustrialEventFactory(
            severity=IndustrialEventSeverity.INFO,
        )

        self.assertEqual(
            event.severity,
            IndustrialEventSeverity.INFO,
        )

    def test_industrial_event_can_be_acknowledged(self):
        user = IndustrialEventFactory().acknowledged_by

        event = IndustrialEventFactory()

        self.assertIsNone(user)
        self.assertIsNone(event.acknowledged_at)
        self.assertIsNone(event.acknowledged_by)

    def test_industrial_event_can_be_resolved(self):
        event = IndustrialEventFactory()

        self.assertIsNone(event.resolved_at)
        self.assertIsNone(event.resolved_by)

    def test_industrial_event_can_have_metadata(self):
        metadata = {
            "source": "plc",
            "sensor_id": "temperature-001",
            "threshold": 80,
        }

        event = IndustrialEventFactory(
            metadata=metadata,
        )

        self.assertEqual(
            event.metadata,
            metadata,
        )

    def test_industrial_event_ordering(self):
        now = timezone.now()

        older_event = IndustrialEventFactory(
            occurred_at=now - timedelta(hours=1),
        )

        newer_event = IndustrialEventFactory(
            occurred_at=now,
        )

        events = list(
            IndustrialEvent.objects.all(),
        )

        self.assertEqual(
            events[0],
            newer_event,
        )

        self.assertEqual(
            events[1],
            older_event,
        )

    def test_acknowledged_user_can_be_null(self):
        event = IndustrialEventFactory(
            acknowledged_by=None,
        )

        self.assertIsNone(
            event.acknowledged_by,
        )

    def test_resolved_user_can_be_null(self):
        event = IndustrialEventFactory(
            resolved_by=None,
        )

        self.assertIsNone(
            event.resolved_by,
        )


class TestTelemetryModel(TestCase):
    def test_create_telemetry(self):
        telemetry = TelemetryFactory()

        self.assertIsNotNone(
            telemetry.id,
        )

        self.assertIsNotNone(
            telemetry.asset,
        )

        self.assertIsNotNone(
            telemetry.metric,
        )

        self.assertIsNotNone(
            telemetry.value,
        )

        self.assertEqual(
            telemetry.quality,
            TelemetryQuality.GOOD,
        )

    def test_telemetry_string_representation(self):
        telemetry = TelemetryFactory(
            metric="temperature",
            value=25.5,
            unit="°C",
        )

        expected = f"{telemetry.asset} - temperature: 25.5 °C"

        self.assertEqual(
            str(telemetry),
            expected,
        )

    def test_telemetry_can_have_empty_unit(self):
        telemetry = TelemetryFactory(
            unit="",
        )

        self.assertEqual(
            telemetry.unit,
            "",
        )

    def test_telemetry_can_have_different_quality_levels(self):
        for quality in TelemetryQuality.values:
            telemetry = TelemetryFactory(
                quality=quality,
            )

            self.assertEqual(
                telemetry.quality,
                quality,
            )

    def test_telemetry_can_have_metadata(self):
        metadata = {
            "source": "sensor",
            "sensor_id": "sensor-001",
            "location": "pump-room",
        }

        telemetry = TelemetryFactory(
            metadata=metadata,
        )

        self.assertEqual(
            telemetry.metadata,
            metadata,
        )

    def test_telemetry_ordering(self):
        now = timezone.now()

        older_telemetry = TelemetryFactory(
            recorded_at=now - timedelta(hours=1),
        )

        newer_telemetry = TelemetryFactory(
            recorded_at=now,
        )

        telemetry_records = list(
            Telemetry.objects.all(),
        )

        self.assertEqual(
            telemetry_records[0],
            newer_telemetry,
        )

        self.assertEqual(
            telemetry_records[1],
            older_telemetry,
        )
