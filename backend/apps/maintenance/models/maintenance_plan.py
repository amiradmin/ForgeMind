from django.db import models

from shared.models.base import BaseModel

from .enums import MaintenanceFrequencyUnit, MaintenanceType


class MaintenancePlan(BaseModel):
    """
    Defines planned and recurring maintenance activities for an asset.
    """

    asset = models.ForeignKey(
        "assets.Asset",
        on_delete=models.PROTECT,
        related_name="maintenance_plans",
    )

    name = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    maintenance_type = models.CharField(
        max_length=30,
        choices=MaintenanceType.choices,
    )

    frequency = models.PositiveIntegerField()

    frequency_unit = models.CharField(
        max_length=20,
        choices=MaintenanceFrequencyUnit.choices,
    )

    start_date = models.DateField()

    next_due_date = models.DateField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "maintenance_plans"
        ordering = ["next_due_date", "name"]

    def __str__(self):
        return self.name
