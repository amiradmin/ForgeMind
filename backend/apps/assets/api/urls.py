from rest_framework.routers import DefaultRouter

from apps.assets.api.views import (
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


urlpatterns = router.urls