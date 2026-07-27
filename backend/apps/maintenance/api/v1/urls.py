from rest_framework.routers import DefaultRouter

from apps.maintenance.api.v1.views import (
    MaintenancePlanViewSet,
    MaintenanceRequestViewSet,
    WorkOrderViewSet,
)

app_name = "maintenance"

router = DefaultRouter()

router.register(
    r"maintenance-plans",
    MaintenancePlanViewSet,
    basename="maintenance-plan",
)

router.register(
    r"maintenance-requests",
    MaintenanceRequestViewSet,
    basename="maintenance-request",
)

router.register(
    r"work-orders",
    WorkOrderViewSet,
    basename="work-order",
)

urlpatterns = router.urls
