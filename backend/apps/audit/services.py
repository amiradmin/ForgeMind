from apps.audit.models import AuditLog


class AuditService:
    """
    Service responsible for creating audit log records.

    This class centralizes audit creation logic so that
    different parts of the application can record user
    activities consistently.
    """

    @staticmethod
    def log(
        *,
        user,
        action,
        instance,
        changes=None,
        request=None,
    ):
        """
        Create an audit log entry.

        Args:
            user:
                User who performed the action.

            action:
                Audit action type from AuditLog.Action.

            instance:
                Django model instance affected by the action.

            changes:
                Dictionary containing changed values.

            request:
                Optional HTTP request used to capture
                IP address and user-agent.

        Returns:
            AuditLog:
                Created audit record.
        """

        ip_address = None
        user_agent = ""

        if request:
            ip_address = request.META.get("REMOTE_ADDR")

            user_agent = request.META.get(
                "HTTP_USER_AGENT",
                "",
            )

        return AuditLog.objects.create(
            user=user,
            action=action,
            model_name=instance.__class__.__name__,
            object_id=instance.id,
            object_repr=str(instance),
            changes=changes or {},
            ip_address=ip_address,
            user_agent=user_agent,
        )
