from decouple import config

from .base import *

DEBUG = config(
    "DEBUG",
    default=True,
    cast=bool,
)


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
