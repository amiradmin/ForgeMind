from django.urls import path

from .views import AssetTimelineAPIView

urlpatterns = [
    path(
        "assets/<uuid:asset_id>/timeline/",
        AssetTimelineAPIView.as_view(),
        name="asset-timeline",
    ),
]
