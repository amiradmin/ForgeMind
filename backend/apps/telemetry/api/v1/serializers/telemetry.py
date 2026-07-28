from rest_framework import serializers

from apps.assets.models import Asset
from apps.telemetry.models import Telemetry


class TelemetrySerializer(serializers.ModelSerializer):
    """
    Serializer for Telemetry.
    """

    asset = serializers.PrimaryKeyRelatedField(
        queryset=Asset.objects.filter(is_active=True),
    )

    class Meta:
        model = Telemetry

        fields = (
            "id",
            "asset",
            "metric",
            "value",
            "unit",
            "quality",
            "recorded_at",
            "metadata",
            "created_at",
        )

        read_only_fields = (
            "id",
            "created_at",
        )
