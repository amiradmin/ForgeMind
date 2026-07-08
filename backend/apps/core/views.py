# Create your views here.
from django.http import JsonResponse


def health_check(request):
    return JsonResponse(
        {
            "status": "ok",
            "service": "ForgeMind Backend",
            "version": "0.1.0",
        }
    )
