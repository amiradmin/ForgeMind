from rest_framework import viewsets

from apps.assets.api.serializers import AssetSerializer
from apps.assets.models import Asset


class AssetViewSet(viewsets.ModelViewSet):
    """
    CRUD API for assets.
    """

    queryset = (
        Asset.objects.select_related(
            "area",
            "area__plant",
            "area__plant__organization",
        )
    )

    serializer_class = AssetSerializer