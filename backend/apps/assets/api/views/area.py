from rest_framework import viewsets

from apps.assets.api.serializers import AreaSerializer
from apps.assets.models import Area


class AreaViewSet(viewsets.ModelViewSet):
    """
    CRUD API for areas.
    """

    queryset = Area.objects.select_related(
        "plant",
        "plant__organization",
    )

    serializer_class = AreaSerializer