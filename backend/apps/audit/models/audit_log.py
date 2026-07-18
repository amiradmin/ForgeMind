from django.conf import settings
from django.db import models

from shared.models.base import BaseModel


class AuditLog(BaseModel):
    """
    Represents a record of a user or system action.

    Audit logs provide a historical trail of important operations
    performed inside the ForgeMind platform.

    Examples of tracked events:

    - Creating an asset
    - Updating asset information
    - Deleting an asset
    - User authentication events

    Attributes:
        user:
            The user who performed the action. Nullable because
            some events may be system-generated.

        action:
            Type of operation performed. Available actions include
            create, update, delete, login, and logout.

        model_name:
            Name of the affected Django model.

        object_id:
            UUID of the affected database object.

        object_repr:
            Human-readable representation of the affected object.

        changes:
            JSON representation of changed fields and values.

        ip_address:
            IP address from which the action was performed.

        user_agent:
            Client information extracted from the request.
    """

    class Action(models.TextChoices):
        CREATE = "create", "Create"
        UPDATE = "update", "Update"
        DELETE = "delete", "Delete"
        LOGIN = "login", "Login"
        LOGOUT = "logout", "Logout"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs",
    )

    action = models.CharField(
        max_length=20,
        choices=Action.choices,
    )

    model_name = models.CharField(
        max_length=100,
    )

    object_id = models.UUIDField(
        null=True,
        blank=True,
    )

    object_repr = models.CharField(
        max_length=255,
        blank=True,
    )

    changes = models.JSONField(
        default=dict,
        blank=True,
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    user_agent = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "audit_logs"
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return f"{self.action} " f"{self.model_name} " f"{self.object_id}"
