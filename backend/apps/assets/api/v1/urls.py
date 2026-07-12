from rest_framework.routers import DefaultRouter

from apps.assets.api.v1.views import (
    AreaViewSet,
    AssetViewSet,
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

router.register(
    r"assets",
    AssetViewSet,
    basename="asset",
)
urlpatterns = router.urls
