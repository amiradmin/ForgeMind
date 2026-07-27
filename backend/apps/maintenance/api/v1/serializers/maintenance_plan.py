from rest_framework import serializers

from apps.assets.models import Asset
from apps.maintenance.models import MaintenancePlan


class MaintenancePlanSerializer(serializers.ModelSerializer):
    """
    Serializer for MaintenancePlan.
    """

    asset = serializers.PrimaryKeyRelatedField(
        queryset=Asset.objects.filter(is_active=True),
    )

    class Meta:
        model = MaintenancePlan

        fields = (
            "id",
            "asset",
            "name",
            "description",
            "maintenance_type",
            "frequency",
            "frequency_unit",
            "start_date",
            "next_due_date",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "next_due_date",
            "created_at",
            "updated_at",
        )
