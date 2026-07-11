from rest_framework.routers import DefaultRouter

from apps.assets.api.views import OrganizationViewSet

app_name = "assets"

router = DefaultRouter()

router.register(
    r"organizations",
    OrganizationViewSet,
    basename="organization",
)

urlpatterns = router.urls