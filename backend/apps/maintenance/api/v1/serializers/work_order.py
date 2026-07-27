from django.contrib.auth import get_user_model
from drf_spectacular.utils import (
    OpenApiExample,
    extend_schema_serializer,
)
from rest_framework import serializers

from apps.assets.models import Asset
from apps.maintenance.models import (
    MaintenanceRequest,
    WorkOrder,
)

User = get_user_model()


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Work Order Request Example",
            value={
                "asset": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
                "maintenance_request": ("8e0a5d9f-3f8b-5d9c-a9a9-234567890bcd"),
                "title": "Repair Main Cooling Pump",
                "description": "Repair the main cooling pump",
                "maintenance_type": "corrective",
                "priority": "high",
                "status": "open",
                "assigned_to": ("9f1b6e8a-4f9c-6d0a-b0aa-345678901cde"),
                "scheduled_start": "2026-07-20T08:00:00Z",
                "scheduled_end": "2026-07-20T12:00:00Z",
                "completion_notes": "",
            },
            request_only=True,
        ),
        OpenApiExample(
            "Work Order Response Example",
            value={
                "id": "1a2b3c4d-5e6f-7a8b-9c0d-123456789abc",
                "asset": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
                "maintenance_request": "8e0a5d9f-3f8b-5d9c-a9a9-234567890bcd",
                "title": "Repair Main Cooling Pump",
                "description": "Repair the main cooling pump",
                "maintenance_type": "corrective",
                "priority": "high",
                "status": "completed",
                "assigned_to": ("9f1b6e8a-4f9c-6d0a-b0aa-345678901cde"),
                "scheduled_start": "2026-07-20T08:00:00Z",
                "scheduled_end": "2026-07-20T12:00:00Z",
                "started_at": "2026-07-20T08:15:00Z",
                "completed_at": "2026-07-20T11:30:00Z",
                "completion_notes": ("Pump repaired and tested successfully."),
                "created_at": "2026-07-19T10:30:00Z",
                "updated_at": "2026-07-20T11:30:00Z",
            },
            response_only=True,
        ),
    ]
)
class WorkOrderSerializer(serializers.ModelSerializer):
    """
    Serializer for WorkOrder.
    """

    asset = serializers.PrimaryKeyRelatedField(
        queryset=Asset.objects.filter(
            is_active=True,
        ),
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
