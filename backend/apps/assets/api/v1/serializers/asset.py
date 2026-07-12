from rest_framework import serializers

from apps.assets.models import Asset


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
