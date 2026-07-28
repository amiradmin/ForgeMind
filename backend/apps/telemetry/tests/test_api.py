from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from apps.telemetry.models.enums import (
    IndustrialEventSeverity,
    IndustrialEventStatus,
    IndustrialEventType,
    TelemetryQuality,
)
from apps.telemetry.tests.factories import (
    IndustrialEventFactory,
    TelemetryFactory,
    UserFactory,
)


class TestIndustrialEventAPI(APITestCase):
    def setUp(self):
        self.user = UserFactory()

        self.client.force_authenticate(
            user=self.user,
        )

        self.event = IndustrialEventFactory()

        self.list_url = reverse(
            "industrial-event-list",
        )

        self.detail_url = reverse(
            "industrial-event-detail",
            kwargs={
                "pk": self.event.pk,
            },
        )

    def test_list_industrial_events(self):
        IndustrialEventFactory()
        IndustrialEventFactory()

        response = self.client.get(
            self.list_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertGreaterEqual(
            len(response.data),
            3,
        )

    def test_retrieve_industrial_event(self):
        response = self.client.get(
            self.detail_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            str(response.data["id"]),
            str(self.event.id),
        )

    def test_create_industrial_event(self):
        payload = {
            "asset": str(
                self.event.asset.id,
            ),
            "event_type": IndustrialEventType.ALARM,
            "severity": IndustrialEventSeverity.HIGH,
            "status": IndustrialEventStatus.OPEN,
            "title": "High Temperature Alarm",
            "description": ("Temperature exceeded the configured threshold."),
            "occurred_at": (timezone.now().isoformat()),
            "metadata": {
                "source": "sensor-001",
                "threshold": 80,
            },
        }

        response = self.client.post(
            self.list_url,
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.data["title"],
            "High Temperature Alarm",
        )

        self.assertEqual(
            response.data["event_type"],
            IndustrialEventType.ALARM,
        )

    def test_delete_industrial_event(self):
        response = self.client.delete(
            self.detail_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertFalse(
            self.event.__class__.objects.filter(
                pk=self.event.pk,
            ).exists(),
        )


class TestTelemetryAPI(APITestCase):
    def setUp(self):
        self.user = UserFactory()

        self.client.force_authenticate(
            user=self.user,
        )

        self.telemetry = TelemetryFactory()

        self.list_url = reverse(
            "telemetry-list",
        )

        self.detail_url = reverse(
            "telemetry-detail",
            kwargs={
                "pk": self.telemetry.pk,
            },
        )

    def test_list_telemetry(self):
        TelemetryFactory()
        TelemetryFactory()

        response = self.client.get(
            self.list_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertGreaterEqual(
            len(response.data),
            3,
        )

    def test_retrieve_telemetry(self):
        response = self.client.get(
            self.detail_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            str(response.data["id"]),
            str(self.telemetry.id),
        )

    def test_create_telemetry(self):
        payload = {
            "asset": str(
                self.telemetry.asset.id,
            ),
            "metric": "temperature",
            "value": 85.5,
            "unit": "°C",
            "quality": TelemetryQuality.GOOD,
            "recorded_at": (timezone.now().isoformat()),
            "metadata": {
                "source": "sensor-001",
                "location": "pump-room",
            },
        }

        response = self.client.post(
            self.list_url,
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.data["metric"],
            "temperature",
        )

        self.assertEqual(
            float(response.data["value"]),
            85.5,
        )

    def test_delete_telemetry(self):
        response = self.client.delete(
            self.detail_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertFalse(
            self.telemetry.__class__.objects.filter(
                pk=self.telemetry.pk,
            ).exists(),
        )
