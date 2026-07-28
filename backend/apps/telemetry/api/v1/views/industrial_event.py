from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.telemetry.api.v1.serializers.industrial_event import (
    IndustrialEventSerializer,
)
from apps.telemetry.models import IndustrialEvent


class IndustrialEventViewSet(ModelViewSet):
    """
    API endpoint for managing industrial events.
    """

    queryset = IndustrialEvent.objects.select_related("asset").all()
    serializer_class = IndustrialEventSerializer
    permission_classes = (IsAuthenticated,)

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    search_fields = (
        "title",
        "description",
        "event_type",
    )

    ordering_fields = (
        "occurred_at",
        "created_at",
        "severity",
    )

    ordering = ("-occurred_at",)

    def get_queryset(self):
        queryset = super().get_queryset()

        asset_id = self.request.query_params.get("asset")
        event_type = self.request.query_params.get("event_type")
        severity = self.request.query_params.get("severity")

        if asset_id:
            queryset = queryset.filter(asset_id=asset_id)

        if event_type:
            queryset = queryset.filter(event_type=event_type)

        if severity:
            queryset = queryset.filter(severity=severity)

        return queryset
