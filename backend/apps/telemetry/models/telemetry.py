import uuid

from django.db import models

from apps.assets.models import Asset

from .enums import TelemetryQuality


class Telemetry(models.Model):
    """
    Represents a telemetry measurement
    produced by an industrial asset.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name="telemetry_records",
    )

    metric = models.CharField(
        max_length=100,
    )

    value = models.FloatField()

    unit = models.CharField(
        max_length=50,
        blank=True,
    )

    quality = models.CharField(
        max_length=20,
        choices=TelemetryQuality.choices,
        default=TelemetryQuality.GOOD,
    )

    recorded_at = models.DateTimeField()

    metadata = models.JSONField(
        default=dict,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ("-recorded_at",)

        indexes = (
            models.Index(
                fields=("asset", "metric", "recorded_at"),
            ),
            models.Index(
                fields=("recorded_at",),
            ),
        )

    def __str__(self):
        return f"{self.asset} - {self.metric}: {self.value} {self.unit}"
