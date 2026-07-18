from rest_framework import serializers

from apps.assets.models import AssetType


class AssetTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for AssetType.
    """

    class Meta:
        model = AssetType

        fields = (
            "id",
            "name",
            "code",
            "description",
            "metadata_schema",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
