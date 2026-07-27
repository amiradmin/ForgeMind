from drf_spectacular.utils import extend_schema

from apps.audit.models import AuditLog
from apps.audit.services import AuditService
from apps.identity.permissions.rbac import HasRBACPermission
from apps.maintenance.api.v1.serializers import WorkOrderSerializer
from apps.maintenance.models import WorkOrder
from shared.views import BaseAPIViewSet


@extend_schema(
    tags=["Work Orders"],
    description="""
    Manage maintenance work orders.

    Work orders represent maintenance work that is
    scheduled, assigned, performed, and completed.
    """,
)
class WorkOrderViewSet(BaseAPIViewSet):
    """
    CRUD API for maintenance work orders.
    """

    serializer_class = WorkOrderSerializer

    permission_classes = [
        HasRBACPermission,
    ]

    action_permissions = {
        "list": "work_order.view",
        "retrieve": "work_order.view",
        "create": "work_order.create",
        "update": "work_order.update",
        "partial_update": "work_order.update",
        "destroy": "work_order.delete",
    }

    filterset_fields = (
        "asset",
        "maintenance_request",
        "maintenance_type",
        "priority",
        "status",
        "assigned_to",
    )

    search_fields = (
        "title",
        "description",
        "completion_notes",
        "asset__name",
        "asset__code",
    )

    ordering_fields = (
        "title",
        "priority",
        "status",
        "scheduled_start",
        "scheduled_end",
        "started_at",
        "completed_at",
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    def get_queryset(self):
        return WorkOrder.objects.select_related(
            "asset",
            "maintenance_request",
            "assigned_to",
        )

    def perform_create(self, serializer):
        work_order = serializer.save()

        AuditService.log(
            user=self.request.user,
            action=AuditLog.Action.CREATE,
            instance=work_order,
            request=self.request,
        )

    def perform_update(self, serializer):
        work_order = serializer.save()

        AuditService.log(
            user=self.request.user,
            action=AuditLog.Action.UPDATE,
            instance=work_order,
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