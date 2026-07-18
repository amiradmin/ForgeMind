from apps.assets.api.v1.serializers import AssetTypeSerializer
from apps.assets.models import AssetType
from shared.views import BaseAPIViewSet


class AssetTypeViewSet(BaseAPIViewSet):
    """
    CRUD API for Asset Types.
    """

    serializer_class = AssetTypeSerializer

    queryset = AssetType.objects.filter(
        is_active=True,
    )

    action_permissions = {
        "list": "asset_type.view",
        "retrieve": "asset_type.view",
        "create": "asset_type.create",
        "update": "asset_type.update",
        "partial_update": "asset_type.update",
        "destroy": "asset_type.delete",
    }

    filterset_fields = ("is_active",)

    search_fields = (
        "name",
        "code",
        "description",
    )

    ordering_fields = (
        "name",
        "code",
        "created_at",
    )

    ordering = ("name",)
