from rest_framework import viewsets

from apps.assets.api.serializers import PlantSerializer
from apps.assets.models import Plant


class PlantViewSet(viewsets.ModelViewSet):
    """
    CRUD API for plants.
    """

    queryset = Plant.objects.select_related("organization")

    serializer_class = PlantSerializer