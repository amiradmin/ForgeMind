from rest_framework import viewsets

from apps.assets.api.serializers import OrganizationSerializer
from apps.assets.models import Organization


class OrganizationViewSet(viewsets.ModelViewSet):
    """CRUD API for organizations."""

    serializer_class = OrganizationSerializer

    def get_queryset(self):
        return (
            Organization.objects.filter(is_active=True)
            .order_by("name")
        )