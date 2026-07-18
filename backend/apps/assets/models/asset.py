from django.db import models

from shared.models.base import BaseModel

from .area import Area


class Asset(BaseModel):
    """
    Physical equipment installed inside an Area.

    Each asset belongs to an AssetType, which defines the
    metadata schema that applies to the asset.
    """

    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        related_name="assets",
    )

    asset_type = models.ForeignKey(
        "assets.AssetType",
        on_delete=models.PROTECT,
        related_name="assets",
    )

    name = models.CharField(
        max_length=200,
    )

    code = models.CharField(
        max_length=50,
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

    metadata = models.JSONField(
        default=dict,
        blank=True,
        help_text="Asset-specific metadata defined by the AssetType schema.",
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
