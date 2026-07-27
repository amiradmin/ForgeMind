from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from apps.assets.models import Asset
from apps.maintenance.models import MaintenancePlan


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Maintenance Plan Request Example",
            value={
                "asset": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
                "name": "Monthly Pump Maintenance",
                "description": "Monthly preventive maintenance for the main cooling pump",
                "maintenance_type": "preventive",
                "frequency": 1,
                "frequency_unit": "months",
                "start_date": "2026-07-01",
            },
            request_only=True,
        ),
        OpenApiExample(
            "Maintenance Plan Response Example",
            value={
                "id": "8e0a5d9f-3f8b-5d9c-a9a9-234567890bcd",
                "asset": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
                "name": "Monthly Pump Maintenance",
                "description": "Monthly preventive maintenance for the main cooling pump",
                "maintenance_type": "preventive",
                "frequency": 1,
                "frequency_unit": "months",
                "start_date": "2026-07-01",
                "next_due_date": "2026-08-01",
                "created_at": "2026-07-01T10:30:00Z",
                "updated_at": "2026-07-01T10:30:00Z",
            },
            response_only=True,
        ),
    ]
)
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
