from rest_framework import serializers


class TimelineEventSerializer(serializers.Serializer):
    """
    Serializer for unified asset operational timeline events.
    """

    type = serializers.CharField()

    timestamp = serializers.DateTimeField()

    title = serializers.CharField()

    data = serializers.JSONField()

    source = serializers.CharField()
