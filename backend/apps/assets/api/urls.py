from rest_framework.routers import DefaultRouter

from apps.assets.api.views import (
    AreaViewSet,
    OrganizationViewSet,
    PlantViewSet,
)

app_name = "assets"

router = DefaultRouter()

router.register(
    r"organizations",
    OrganizationViewSet,
    basename="organization",
)

router.register(
    r"plants",
    PlantViewSet,
    basename="plant",
)

router.register(
    r"areas",
    AreaViewSet,
    basename="area",
)
urlpatterns = router.urls