from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    # Core
    path(
        "api/v1/",
        include("apps.core.api.v1.urls"),
    ),

    # Authentication
    path(
        "api/v1/auth/",
        include("apps.identity.urls"),
    ),

    # Assets
    path(
        "api/v1/",
        include("apps.assets.api.v1.urls"),
    ),


    # OpenAPI schema
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    # Swagger
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),

    # Redoc
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(
            url_name="schema"
        ),
        name="redoc",
    ),
]