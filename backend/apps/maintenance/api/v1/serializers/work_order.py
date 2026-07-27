from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.assets.models import Asset
from apps.maintenance.models import MaintenanceRequest, WorkOrder

User = get_user_model()


class WorkOrderSerializer(serializers.ModelSerializer):
    """
    Serializer for WorkOrder.
    """

    asset = serializers.PrimaryKeyRelatedField(
        queryset=Asset.objects.filter(is_active=True),
    )

    maintenance_request = serializers.PrimaryKeyRelatedField(
        queryset=MaintenanceRequest.objects.all(),
        required=False,
        allow_null=True,
    )

    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = WorkOrder

        fields = (
            "id",
            "asset",
            "maintenance_request",
            "title",
            "description",
            "maintenance_type",
            "priority",
            "status",
            "assigned_to",
            "scheduled_start",
            "scheduled_end",
            "started_at",
            "completed_at",
            "completion_notes",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
