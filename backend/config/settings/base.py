from datetime import timedelta
from pathlib import Path

from decouple import config

# ------------------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ------------------------------------------------------------------------------
# Core
# ------------------------------------------------------------------------------

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="localhost,127.0.0.1",
    cast=lambda v: [host.strip() for host in v.split(",")],
)

# ------------------------------------------------------------------------------
# Applications
# ------------------------------------------------------------------------------

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "django_filters",
    "drf_spectacular",
]

LOCAL_APPS = [
    "apps.core",
    "apps.identity",
    # "apps.assets",
    "apps.assets.apps.AssetsConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ------------------------------------------------------------------------------
# Middleware
# ------------------------------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "shared.middleware.request_logging.RequestLoggingMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ------------------------------------------------------------------------------
# URLs
# ------------------------------------------------------------------------------

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"

# ------------------------------------------------------------------------------
# Templates
# ------------------------------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ------------------------------------------------------------------------------
# Database
# ------------------------------------------------------------------------------


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
    }
}

# ------------------------------------------------------------------------------
# Redis
# ------------------------------------------------------------------------------

REDIS_URL = config(
    "REDIS_URL",
    default="redis://localhost:6379/0",
)

# ------------------------------------------------------------------------------
# Password Validation
# ------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
AUTH_USER_MODEL = "identity.User"
# ------------------------------------------------------------------------------
# Internationalization
# ------------------------------------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True

# ------------------------------------------------------------------------------
# Static & Media
# ------------------------------------------------------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------------------------------------------------------------
# Default PK
# ------------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------------------------------------------------------------
# Django REST Framework
# ------------------------------------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "DEFAULT_VERSION": "v1",
    "ALLOWED_VERSIONS": [
        "v1",
    ],
    "VERSION_PARAM": "version",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": ("rest_framework.pagination.PageNumberPagination"),
    "DEFAULT_SCHEMA_CLASS": ("drf_spectacular.openapi.AutoSchema"),
    "PAGE_SIZE": 20,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        days=config(
            "JWT_ACCESS_TOKEN_DAYS",
            default=1,
            cast=int,
        )
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=config(
            "JWT_REFRESH_TOKEN_DAYS",
            default=7,
            cast=int,
        )
    ),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
}

APP_NAME = "ForgeMind"
APP_VERSION = "1.0.0"




# ------------------------------------------------------------------------------
# drf-spectacular OpenAPI Documentation
# ------------------------------------------------------------------------------
SPECTACULAR_SETTINGS = {

    "TITLE": "ForgeMind API",

    "DESCRIPTION": """
ForgeMind Industrial AI Platform API.

Provides:

- Identity management
- Organization management
- Industrial assets
- AI services
""",

    "VERSION": APP_VERSION,


    "COMPONENT_SPLIT_REQUEST": True,


    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",


    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "displayOperationId": True,
        "filter": True,
        "persistAuthorization": True,
    },


    

    "APPEND_COMPONENTS": {

        "securitySchemes": {
            "jwtAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
    },


    "TAGS": [
        {
            "name": "Authentication",
            "description": "JWT authentication endpoints.",
        },
        {
            "name": "Organizations",
            "description": "Manage industrial organizations.",
        },
        {
            "name": "Plants",
            "description": "Manage industrial plants.",
        },
        {
            "name": "Areas",
            "description": "Manage production areas.",
        },
        {
            "name": "Assets",
            "description": "Manage industrial assets.",
        },
        {
            "name": "System",
            "description": "System monitoring endpoints.",
        },
    ],
}