import uuid

from django.conf import settings
from django.db import models

from apps.assets.models import Asset

from .enums import (
    IndustrialEventSeverity,
    IndustrialEventStatus,
    IndustrialEventType,
)


class IndustrialEvent(models.Model):
    """
    Represents an operational or industrial event associated
    with an industrial asset.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name="industrial_events",
    )

    event_type = models.CharField(
        max_length=30,
        choices=IndustrialEventType.choices,
    )

    severity = models.CharField(
        max_length=20,
        choices=IndustrialEventSeverity.choices,
        default=IndustrialEventSeverity.INFO,
    )

    status = models.CharField(
        max_length=20,
        choices=IndustrialEventStatus.choices,
        default=IndustrialEventStatus.OPEN,
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    occurred_at = models.DateTimeField()

    acknowledged_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    resolved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    acknowledged_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="acknowledged_industrial_events",
        null=True,
        blank=True,
    )

    resolved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="resolved_industrial_events",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ("-occurred_at",)

        indexes = (
            models.Index(
                fields=("asset", "occurred_at"),
            ),
            models.Index(
                fields=("event_type", "status"),
            ),
            models.Index(
                fields=("severity", "status"),
            ),
        )

    def __str__(self):
        return f"{self.asset} - {self.title}"
