from django.contrib import admin

from .models import Organization, Plant


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "code",
    )


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "organization",
        "code",
        "city",
        "country",
        "is_active",
    )

    list_filter = (
        "organization",
        "country",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "city",
    )