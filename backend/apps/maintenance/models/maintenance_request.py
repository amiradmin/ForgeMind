from django.conf import settings
from django.db import models
from django.utils import timezone

from shared.models.base import BaseModel

from .enums import MaintenancePriority, MaintenanceRequestStatus, MaintenanceType


class MaintenanceRequest(BaseModel):
    """
    Represents a maintenance need or request for an asset.
    """

    asset = models.ForeignKey(
        "assets.Asset",
        on_delete=models.PROTECT,
        related_name="maintenance_requests",
    )

    maintenance_plan = models.ForeignKey(
        "maintenance.MaintenancePlan",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="requests",
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    maintenance_type = models.CharField(
        max_length=30,
        choices=MaintenanceType.choices,
    )

    priority = models.CharField(
        max_length=20,
        choices=MaintenancePriority.choices,
        default=MaintenancePriority.MEDIUM,
    )

    status = models.CharField(
        max_length=20,
        choices=MaintenanceRequestStatus.choices,
        default=MaintenanceRequestStatus.OPEN,
    )

    requested_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="maintenance_requests",
    )

    requested_at = models.DateTimeField(
        default=timezone.now,
    )

    resolved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "maintenance_requests"
        ordering = ["-requested_at"]

    def __str__(self):
        return self.title