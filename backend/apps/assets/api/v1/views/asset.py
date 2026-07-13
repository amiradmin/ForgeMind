from apps.assets.api.v1.serializers import AssetSerializer
from apps.assets.models import Asset
from apps.identity.permissions.rbac import HasRBACPermission
from shared.views import BaseAPIViewSet


class AssetViewSet(BaseAPIViewSet):
    """
    CRUD API for assets.
    """

    serializer_class = AssetSerializer
    permission_classes = [
        HasRBACPermission,
    ]

    action_permissions = {
        "list": "asset.view",
        "retrieve": "asset.view",
        "create": "asset.create",
        "update": "asset.update",
        "partial_update": "asset.update",
        "destroy": "asset.delete",
    }

    filterset_fields = (
        "area",
        "asset_type",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "manufacturer",
        "model",
        "serial_number",
        "area__name",
        "area__plant__name",
        "area__plant__organization__name",
    )

    ordering_fields = (
        "name",
        "code",
        "installation_date",
        "created_at",
    )

    ordering = ("name",)

    def get_queryset(self):
        return Asset.objects.select_related(
            "area",
            "area__plant",
            "area__plant__organization",
        ).filter(is_active=True)
