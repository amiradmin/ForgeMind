from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.assets.models import Asset
from apps.maintenance.models import MaintenancePlan, MaintenanceRequest

User = get_user_model()


class MaintenanceRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for MaintenanceRequest.
    """

    asset = serializers.PrimaryKeyRelatedField(
        queryset=Asset.objects.filter(is_active=True),
    )

    maintenance_plan = serializers.PrimaryKeyRelatedField(
        queryset=MaintenancePlan.objects.all(),
        required=False,
        allow_null=True,
    )

    requested_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = MaintenanceRequest

        fields = (
            "id",
            "asset",
            "maintenance_plan",
            "title",
            "description",
            "maintenance_type",
            "priority",
            "status",
            "requested_by",
            "requested_at",
            "resolved_at",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "requested_at",
            "created_at",
            "updated_at",
        )