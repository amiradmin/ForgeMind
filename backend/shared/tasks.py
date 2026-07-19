"""
Shared background tasks used across ForgeMind.
"""

from celery import shared_task


@shared_task
def health_check_task():
    """
    Simple Celery health check task.

    Used to verify that Celery worker is running correctly.
    """

    return {
        "status": "ok",
        "message": "Celery worker is running",
    }