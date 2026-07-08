from django.db import models

from shared.models.base import BaseModel
from .plant import Plant


class Area(BaseModel):
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        related_name="areas",
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("plant", "code")

    def __str__(self):
        return self.name