"""
Celery configuration for ForgeMind.

This module initializes the Celery application and loads
Django settings for background task execution.
"""

import os

from celery import Celery


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings.development",
)


app = Celery(
    "forgemind",
)


app.config_from_object(
    "django.conf:settings",
    namespace="CELERY",
)


app.autodiscover_tasks()