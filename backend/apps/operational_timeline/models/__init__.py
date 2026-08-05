"""
Operational Timeline models package.

This application does not define database models.
It aggregates operational data from existing domains:

- Assets
- Telemetry
- Maintenance
- Audit
- AI Predictions
"""

from .operational_event import OperationalEvent

__all__ = [
    "OperationalEvent",
]
