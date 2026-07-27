from drf_spectacular.utils import extend_schema

from apps.audit.models import AuditLog
from apps.audit.services import AuditService
from apps.identity.permissions.rbac import HasRBACPermission
from apps.maintenance.api.v1.serializers import MaintenancePlanSerializer
from apps.maintenance.models import MaintenancePlan
from apps.maintenance.services import MaintenancePlanService
from shared.views import BaseAPIViewSet


@extend_schema(
    tags=["Maintenance Plans"],
    description="""
    Manage preventive and recurring maintenance plans.

    Maintenance plans define scheduled maintenance activities
    for industrial assets.
    """,
)
class MaintenancePlanViewSet(BaseAPIViewSet):
    """
    CRUD API for maintenance plans.
    """

    serializer_class = MaintenancePlanSerializer

    permission_classes = [
        HasRBACPermission,
    ]

    action_permissions = {
        "list": "maintenance_plan.view",
        "retrieve": "maintenance_plan.view",
        "create": "maintenance_plan.create",
        "update": "maintenance_plan.update",
        "partial_update": "maintenance_plan.update",
        "destroy": "maintenance_plan.delete",
    }

    filterset_fields = (
        "asset",
        "maintenance_type",
        "frequency_unit",
    )

    search_fields = (
        "name",
        "description",
        "asset__name",
        "asset__code",
    )

    ordering_fields = (
        "name",
        "start_date",
        "next_due_date",
        "created_at",
    )

    ordering = (
        "next_due_date",
        "name",
    )

    def get_queryset(self):
        return MaintenancePlan.objects.select_related(
            "asset",
        )

    def perform_create(self, serializer):
        plan = MaintenancePlanService.create_plan(
            **serializer.validated_data,
        )

        serializer.instance = plan

        AuditService.log(
            user=self.request.user,
            action=AuditLog.Action.CREATE,
            instance=plan,
            request=self.request,
        )

    def perform_update(self, serializer):
        plan = serializer.save()

        AuditService.log(
            user=self.request.user,
            action=AuditLog.Action.UPDATE,
            instance=plan,
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