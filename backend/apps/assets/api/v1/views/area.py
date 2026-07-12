from apps.assets.api.v1.serializers import AreaSerializer
from apps.assets.models import Area
from shared.views import BaseAPIViewSet


class AreaViewSet(BaseAPIViewSet):
    """
    CRUD API for areas.
    """

    serializer_class = AreaSerializer

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
