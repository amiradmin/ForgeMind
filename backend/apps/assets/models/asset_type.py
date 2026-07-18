from django.db import models

from shared.models.base import BaseModel


class AssetType(BaseModel):
    """
    Defines a category of industrial assets.

    Examples:
    - Pump
    - Motor
    - Sensor
    - Compressor

    Each AssetType defines the metadata schema that assets of this
    type are expected to follow.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    metadata_schema = models.JSONField(
        default=dict,
        blank=True,
        help_text="JSON schema describing supported metadata.",
    )

    class Meta:
        db_table = "asset_types"
        ordering = ["name"]

    def __str__(self):
        return self.name
