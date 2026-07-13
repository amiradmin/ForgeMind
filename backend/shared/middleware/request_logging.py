import logging
import time

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """
    Logs every HTTP request and its response.

    Example:
    [2026-07-13 12:35:18] INFO shared.middleware.request_logging
    GET /api/v1/assets/ 200 14.32ms 127.0.0.1
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()

        response = self.get_response(request)

        duration_ms = (time.perf_counter() - start_time) * 1000

        client_ip = request.META.get("REMOTE_ADDR", "-")

        logger.info(
            "%s %s %s %.2fms %s",
            request.method,
            request.get_full_path(),
            response.status_code,
            duration_ms,
            client_ip,
        )

        return response
