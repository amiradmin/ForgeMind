from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets


class BaseAPIViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet for ForgeMind APIs.
    """

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )