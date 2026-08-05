from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.assets.models import Asset
from apps.operational_timeline.api.v1.serializers import (
    TimelineEventSerializer,
)
from apps.operational_timeline.services.timeline_service import (
    AssetTimelineService,
)


class AssetTimelineAPIView(APIView):
    """
    Returns operational timeline for an asset.
    """

    def get(self, request, asset_id):

        asset = get_object_or_404(
            Asset,
            id=asset_id,
        )

        events = AssetTimelineService.get_timeline(
            asset,
        )

        serializer = TimelineEventSerializer(
            events,
            many=True,
        )

        return Response(serializer.data)
