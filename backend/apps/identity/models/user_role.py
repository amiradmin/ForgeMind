from django.conf import settings
from django.db import models


class UserRole(models.Model):
    """
    Associates users with roles.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_roles",
    )

    role = models.ForeignKey(
        "identity.Role",
        on_delete=models.CASCADE,
        related_name="user_roles",
    )

    class Meta:
        unique_together = ("user", "role")

    def __str__(self):
        return f"{self.user} -> {self.role}"
