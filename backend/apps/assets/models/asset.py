from django.db import models

from shared.models.base import BaseModel

from .area import Area


class Asset(BaseModel):
    """
    Physical equipment inside an Area.
    """

    class AssetType(models.TextChoices):
        MOTOR = "motor", "Motor"
        PUMP = "pump", "Pump"
        VALVE = "valve", "Valve"
        SENSOR = "sensor", "Sensor"
        PLC = "plc", "PLC"
        CONVEYOR = "conveyor", "Conveyor"
        OTHER = "other", "Other"

    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        related_name="assets",
    )

    name = models.CharField(
        max_length=200,
    )

    code = models.CharField(
        max_length=50,
    )

    asset_type = models.CharField(
        max_length=30,
        choices=AssetType.choices,
        default=AssetType.OTHER,
    )

    manufacturer = models.CharField(
        max_length=100,
        blank=True,
    )

    model = models.CharField(
        max_length=100,
        blank=True,
    )

    serial_number = models.CharField(
        max_length=100,
        blank=True,
    )

    installation_date = models.DateField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "assets"
        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["area", "code"],
                name="unique_area_asset_code",
            )
        ]

    def __str__(self):
        return self.name
