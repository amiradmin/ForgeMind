from apps.assets.api.v1.serializers import OrganizationSerializer
from apps.assets.models import Organization
from apps.identity.permissions.rbac import HasRBACPermission
from shared.views import BaseAPIViewSet


class OrganizationViewSet(BaseAPIViewSet):
    """CRUD API for organizations."""

    serializer_class = OrganizationSerializer

    permission_classes = [
        HasRBACPermission,
    ]

    action_permissions = {
        "list": "organization.view",
        "retrieve": "organization.view",
        "create": "organization.create",
        "update": "organization.update",
        "partial_update": "organization.update",
        "destroy": "organization.delete",
    }

    filterset_fields = ("is_active",)

    search_fields = ("name",)

    ordering_fields = (
        "name",
        "created_at",
    )

    ordering = ("name",)

    def get_queryset(self):
        return Organization.objects.filter(is_active=True)
