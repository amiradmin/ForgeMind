from django.contrib import admin

from apps.audit.models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    """
    Django admin configuration for AuditLog.

    Provides administrators with the ability to inspect
    system activity history.

    Features:

    - Filtering by action and model
    - Searching by object representation
    - Displaying responsible user and timestamp
    """

    list_display = (
        "action",
        "model_name",
        "object_id",
        "user",
        "created_at",
    )

    list_filter = (
        "action",
        "model_name",
        "created_at",
    )

    search_fields = (
        "object_repr",
        "user__email",
    )
