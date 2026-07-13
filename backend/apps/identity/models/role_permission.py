from django.db import models


class RolePermission(models.Model):
    """
    Associates roles with permissions.
    """

    role = models.ForeignKey(
        "identity.Role",
        on_delete=models.CASCADE,
        related_name="role_permissions",
    )

    permission = models.ForeignKey(
        "identity.Permission",
        on_delete=models.CASCADE,
        related_name="role_permissions",
    )

    class Meta:
        unique_together = ("role", "permission")

    def __str__(self):
        return f"{self.role} -> {self.permission}"
