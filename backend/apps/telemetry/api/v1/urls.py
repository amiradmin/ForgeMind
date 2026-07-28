from rest_framework.routers import DefaultRouter

from apps.telemetry.api.v1.views.industrial_event import (
    IndustrialEventViewSet,
)
from apps.telemetry.api.v1.views.telemetry import (
    TelemetryViewSet,
)

router = DefaultRouter()

router.register(
    "industrial-events",
    IndustrialEventViewSet,
    basename="industrial-event",
)

router.register(
    "telemetry",
    TelemetryViewSet,
    basename="telemetry",
)

urlpatterns = router.urls
