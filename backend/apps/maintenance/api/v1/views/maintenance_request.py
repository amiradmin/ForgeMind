from drf_spectacular.utils import extend_schema

from apps.audit.models import AuditLog
from apps.audit.services import AuditService
from apps.identity.permissions.rbac import HasRBACPermission
from apps.maintenance.api.v1.serializers import MaintenanceRequestSerializer
from apps.maintenance.models import MaintenanceRequest
from shared.views import BaseAPIViewSet


@extend_schema(
    tags=["Maintenance Requests"],
    description="""
    Manage maintenance requests.

    Maintenance requests represent maintenance needs
    reported for industrial assets.
    """,
)
class MaintenanceRequestViewSet(BaseAPIViewSet):
    """
    CRUD API for maintenance requests.
    """

    serializer_class = MaintenanceRequestSerializer

    permission_classes = [
        HasRBACPermission,
    ]

    action_permissions = {
        "list": "maintenance_request.view",
        "retrieve": "maintenance_request.view",
        "create": "maintenance_request.create",
        "update": "maintenance_request.update",
        "partial_update": "maintenance_request.update",
        "destroy": "maintenance_request.delete",
    }

    filterset_fields = (
        "asset",
        "maintenance_plan",
        "maintenance_type",
        "priority",
        "status",
    )

    search_fields = (
        "title",
        "description",
        "asset__name",
        "asset__code",
    )

    ordering_fields = (
        "title",
        "priority",
        "status",
        "requested_at",
        "resolved_at",
        "created_at",
    )

    ordering = ("-requested_at",)

    def get_queryset(self):
        return MaintenanceRequest.objects.select_related(
            "asset",
            "maintenance_plan",
            "requested_by",
        )

    def perform_create(self, serializer):
        request = serializer.save(
            requested_by=self.request.user,
        )

        AuditService.log(
            user=self.request.user,
            action=AuditLog.Action.CREATE,
            instance=request,
            request=self.request,
        )

    def perform_update(self, serializer):
        maintenance_request = serializer.save()

        AuditService.log(
            user=self.request.user,
            action=AuditLog.Action.UPDATE,
            instance=maintenance_request,
            request=self.request,
        )

    def perform_destroy(self, instance):
        AuditService.log(
            user=self.request.user,
            action=AuditLog.Action.DELETE,
            instance=instance,
            request=self.request,
        )

        instance.delete()
