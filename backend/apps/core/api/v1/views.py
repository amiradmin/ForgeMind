import logging
from datetime import UTC, datetime

from django.conf import settings
from django.db import connection
from django.db.utils import OperationalError
from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
)
from rest_framework import permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class HealthCheckSerializer(serializers.Serializer):
    status = serializers.CharField()
    service = serializers.CharField()
    version = serializers.CharField()
    timestamp = serializers.DateTimeField()
    checks = serializers.DictField()


class HealthCheckAPIView(APIView):
    """
    System health check endpoint.
    """

    permission_classes = [
        permissions.AllowAny,
    ]

    @extend_schema(
        tags=["System"],
        auth=[],
        summary="System health check",
        description="""
Check the health status of ForgeMind services.

This endpoint verifies:

- Application availability
- Database connectivity

Used by:

- Monitoring systems
- Load balancers
- Deployment health checks
""",
        responses={
            200: OpenApiResponse(
                response=HealthCheckSerializer,
                description="System is healthy",
            ),
            503: OpenApiResponse(
                response=HealthCheckSerializer,
                description="System is unhealthy",
            ),
        },
    )
    def get(self, request):
        checks = {}

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")

            checks["database"] = "ok"
            overall_status = "healthy"
            http_status = status.HTTP_200_OK

        except OperationalError:
            checks["database"] = "error"
            overall_status = "unhealthy"
            http_status = status.HTTP_503_SERVICE_UNAVAILABLE

        logger.info(
            "Health check requested",
            extra={
                "status": overall_status,
                "checks": checks,
            },
        )

        return Response(
            {
                "status": overall_status,
                "service": "ForgeMind",
                "version": getattr(
                    settings,
                    "APP_VERSION",
                    "1.0.0",
                ),
                "timestamp": datetime.now(UTC).isoformat(),
                "checks": checks,
            },
            status=http_status,
        )