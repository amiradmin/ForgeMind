from drf_spectacular.utils import extend_schema

from apps.assets.api.v1.serializers import PlantSerializer
from apps.assets.models import Plant
from apps.identity.permissions.rbac import HasRBACPermission
from shared.views import BaseAPIViewSet


@extend_schema(
    tags=["Plants"],
    description="""
    Manage industrial plants.

    Plants belong to organizations and contain
    multiple operational areas.
    """,
)
class PlantViewSet(BaseAPIViewSet):
    """
    CRUD API for plants.
    """

    serializer_class = PlantSerializer
    permission_classes = [
        HasRBACPermission,
    ]

    action_permissions = {
        "list": "plant.view",
        "retrieve": "plant.view",
        "create": "plant.create",
        "update": "plant.update",
        "partial_update": "plant.update",
        "destroy": "plant.delete",
    }

    filterset_fields = (
        "organization",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "organization__name",
    )

    ordering_fields = (
        "name",
        "code",
        "created_at",
    )

    ordering = ("name",)

    def get_queryset(self):
        return Plant.objects.select_related("organization").filter(is_active=True)
