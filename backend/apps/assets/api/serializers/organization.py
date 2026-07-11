from rest_framework import serializers

from apps.assets.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer for Organization."""

    class Meta:
        model = Organization

        fields = (
            "id",
            "name",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )