from apps.assets.models import Asset


class AssetTimelineService:
    """
    Aggregates operational events related to an asset.

    Data sources:
    - Telemetry
    - Maintenance
    """

    @staticmethod
    def get_timeline(asset: Asset):
        events = []

        events.extend(AssetTimelineService._get_telemetry_events(asset))

        events.extend(AssetTimelineService._get_maintenance_events(asset))

        return sorted(
            events,
            key=lambda event: event["timestamp"],
            reverse=True,
        )

    @staticmethod
    def _get_telemetry_events(asset: Asset):
        return [
            {
                "type": "telemetry",
                "timestamp": telemetry.recorded_at,
                "title": telemetry.metric,
                "data": {
                    "value": telemetry.value,
                    "unit": telemetry.unit,
                    "quality": telemetry.quality,
                },
                "source": "telemetry",
            }
            for telemetry in asset.telemetry_records.all()
        ]

    @staticmethod
    def _get_maintenance_events(asset: Asset):
        return [
            {
                "type": "maintenance",
                "timestamp": maintenance.requested_at,
                "title": maintenance.title,
                "data": {
                    "status": maintenance.status,
                    "priority": maintenance.priority,
                },
                "source": "maintenance",
            }
            for maintenance in asset.maintenance_requests.all()
        ]
