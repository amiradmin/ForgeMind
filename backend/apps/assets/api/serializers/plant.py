from rest_framework import serializers

from apps.assets.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    """Serializer for Plant."""

    class Meta:
        model = Plant

        fields = (
            "id",
            "organization",
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
