from django.db import models

from shared.models.base import BaseModel

from .organization import Organization


class Plant(BaseModel):
    """
    Industrial plant or facility.
    """

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="plants",
    )

    name = models.CharField(
        max_length=200,
    )

    code = models.CharField(
        max_length=50,
    )

    address = models.TextField(
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "plants"
        ordering = ["name"]
        verbose_name = "Plant"
        verbose_name_plural = "Plants"
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code"],
                name="unique_organization_plant_code",
            )
        ]

    def __str__(self):
        return f"{self.organization.name} - {self.name}"