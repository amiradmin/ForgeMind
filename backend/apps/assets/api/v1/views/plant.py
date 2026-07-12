from apps.assets.api.v1.serializers import PlantSerializer
from apps.assets.models import Plant
from shared.views import BaseAPIViewSet


class PlantViewSet(BaseAPIViewSet):
    """
    CRUD API for plants.
    """

    serializer_class = PlantSerializer

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
