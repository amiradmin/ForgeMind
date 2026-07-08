from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "email",
        "username",
    )

    ordering = ("email",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "ForgeMind",
            {
                "fields": (
                    "phone_number",
                    "job_title",
                ),
            },
        ),
    )
