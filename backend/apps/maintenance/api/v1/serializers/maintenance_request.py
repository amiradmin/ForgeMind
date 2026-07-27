from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from apps.assets.models import Asset
from apps.maintenance.models import MaintenancePlan, MaintenanceRequest

User = get_user_model()


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Maintenance Request Example",
            value={
                "asset": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
                "maintenance_plan": None,
                "title": "Main Pump Failure",
                "description": "The main cooling pump is not working",
                "maintenance_type": "corrective",
                "priority": "high",
                "status": "open",
            },
            request_only=True,
        ),
        OpenApiExample(
            "Maintenance Request Response Example",
            value={
                "id": "8e0a5d9f-3f8b-5d9c-a9a9-234567890bcd",
                "asset": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
                "maintenance_plan": None,
                "title": "Main Pump Failure",
                "description": "The main cooling pump is not working",
                "maintenance_type": "corrective",
                "priority": "high",
                "status": "open",
                "requested_by": "9f1b6e8a-4f9c-6d0a-b0aa-345678901cde",
                "requested_at": "2026-07-01T10:30:00Z",
                "resolved_at": None,
                "created_at": "2026-07-01T10:30:00Z",
                "updated_at": "2026-07-01T10:30:00Z",
            },
            response_only=True,
        ),
    ]
)
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
