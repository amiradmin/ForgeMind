from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.telemetry.api.v1.serializers.telemetry import (
    TelemetrySerializer,
)
from apps.telemetry.models import Telemetry


class TelemetryViewSet(ModelViewSet):
    """
    API endpoint for managing telemetry records.
    """

    queryset = Telemetry.objects.select_related("asset").all()
    serializer_class = TelemetrySerializer
    permission_classes = (IsAuthenticated,)

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    search_fields = (
        "metric",
        "unit",
    )

    ordering_fields = (
        "recorded_at",
        "created_at",
        "value",
    )

    ordering = ("-recorded_at",)

    def get_queryset(self):
        queryset = super().get_queryset()

        asset_id = self.request.query_params.get("asset")
        metric = self.request.query_params.get("metric")

        if asset_id:
            queryset = queryset.filter(asset_id=asset_id)

        if metric:
            queryset = queryset.filter(metric=metric)

        return queryset
