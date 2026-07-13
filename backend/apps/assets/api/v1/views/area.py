from apps.assets.api.v1.serializers import AreaSerializer
from apps.assets.models import Area
from shared.permissions.rbac import HasRBACPermission
from shared.views import BaseAPIViewSet


class AreaViewSet(BaseAPIViewSet):
    """
    CRUD API for areas.
    """

    serializer_class = AreaSerializer

    permission_classes = [HasRBACPermission]

    action_permissions = {
        "list": "area.view",
        "retrieve": "area.view",
        "create": "area.create",
        "update": "area.update",
        "partial_update": "area.update",
        "destroy": "area.delete",
    }

    filterset_fields = (
        "plant",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "plant__name",
        "plant__organization__name",
    )

    ordering_fields = (
        "name",
        "code",
        "created_at",
    )

    ordering = ("name",)

    def get_queryset(self):
        return Area.objects.select_related(
            "plant",
            "plant__organization",
        ).filter(is_active=True)
