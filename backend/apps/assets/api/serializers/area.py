from rest_framework import serializers

from apps.assets.models import Area


class AreaSerializer(serializers.ModelSerializer):
    """Serializer for Area."""

    class Meta:
        model = Area

        fields = (
            "id",
            "plant",
            "name",
            "code",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )