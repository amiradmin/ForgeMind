from django.conf import settings
from django.db import models

from shared.models.base import BaseModel

from .enums import MaintenancePriority, MaintenanceType, WorkOrderStatus


class WorkOrder(BaseModel):
    """
    Represents maintenance work to be performed or completed for an asset.
    """

    asset = models.ForeignKey(
        "assets.Asset",
        on_delete=models.PROTECT,
        related_name="work_orders",
    )

    maintenance_request = models.ForeignKey(
        "maintenance.MaintenanceRequest",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="work_orders",
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
        choices=WorkOrderStatus.choices,
        default=WorkOrderStatus.OPEN,
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_work_orders",
    )

    scheduled_start = models.DateTimeField(
        null=True,
        blank=True,
    )

    scheduled_end = models.DateTimeField(
        null=True,
        blank=True,
    )

    started_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    completion_notes = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "work_orders"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
