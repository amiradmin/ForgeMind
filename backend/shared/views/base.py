from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from apps.identity.permissions.rbac import HasRBACPermission


class BaseAPIViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet for ForgeMind APIs.
    """

    permission_classes = [
        HasRBACPermission,
    ]

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )