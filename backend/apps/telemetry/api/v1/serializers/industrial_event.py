from rest_framework import serializers

from apps.assets.models import Asset
from apps.telemetry.models import IndustrialEvent


class IndustrialEventSerializer(serializers.ModelSerializer):
    """
    Serializer for IndustrialEvent.
    """

    asset = serializers.PrimaryKeyRelatedField(
        queryset=Asset.objects.filter(is_active=True),
    )

    class Meta:
        model = IndustrialEvent

        fields = (
            "id",
            "asset",
            "event_type",
            "severity",
            "status",
            "title",
            "description",
            "occurred_at",
            "acknowledged_at",
            "resolved_at",
            "acknowledged_by",
            "resolved_by",
            "metadata",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "acknowledged_at",
            "resolved_at",
            "acknowledged_by",
            "resolved_by",
            "created_at",
            "updated_at",
        )
