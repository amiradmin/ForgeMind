from django.db import models


class TelemetryQuality(models.TextChoices):
    GOOD = "good", "Good"
    UNCERTAIN = "uncertain", "Uncertain"
    BAD = "bad", "Bad"


class IndustrialEventType(models.TextChoices):
    ALARM = "alarm", "Alarm"
    FAILURE = "failure", "Failure"
    WARNING = "warning", "Warning"
    STATE_CHANGE = "state_change", "State Change"
    MAINTENANCE = "maintenance", "Maintenance"
    OPERATIONAL = "operational", "Operational"


class IndustrialEventSeverity(models.TextChoices):
    INFO = "info", "Info"
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    CRITICAL = "critical", "Critical"


class IndustrialEventStatus(models.TextChoices):
    OPEN = "open", "Open"
    ACKNOWLEDGED = "acknowledged", "Acknowledged"
    RESOLVED = "resolved", "Resolved"
    CLOSED = "closed", "Closed"
