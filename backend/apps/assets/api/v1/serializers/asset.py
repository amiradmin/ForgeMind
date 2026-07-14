from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from apps.assets.models import Asset


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Industrial Pump Asset Example",
            value={
                "area": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
                "name": "Main Cooling Pump",
                "code": "PUMP-001",
                "asset_type": "pump",
                "manufacturer": "Siemens",
                "model": "SIPOS 7",
                "serial_number": "SN-2026-001",
                "installation_date": "2026-01-15",
                "is_active": True,
            },
            request_only=True,
        ),
        OpenApiExample(
            "Asset Response Example",
            value={
                "id": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
                "area": "7d9f4c8e-2f7a-4c9b-9a8a-123456789abc",
                "name": "Main Cooling Pump",
                "code": "PUMP-001",
                "asset_type": "pump",
                "manufacturer": "Siemens",
                "model": "SIPOS 7",
                "serial_number": "SN-2026-001",
                "installation_date": "2026-01-15",
                "is_active": True,
                "created_at": "2026-07-14T10:30:00Z",
                "updated_at": "2026-07-14T10:30:00Z",
            },
            response_only=True,
        ),
    ]
)
class AssetSerializer(serializers.ModelSerializer):
    """Serializer for Asset."""

    class Meta:
        model = Asset

        fields = (
            "id",
            "area",
            "name",
            "code",
            "asset_type",
            "manufacturer",
            "model",
            "serial_number",
            "installation_date",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )