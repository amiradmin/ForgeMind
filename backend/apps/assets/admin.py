from django.contrib import admin

from .models import Organization, Plant, Area, Asset



@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "code")
    list_filter = ("organization",)
    search_fields = ("name", "code")


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name", "plant", "code")
    list_filter = ("plant",)
    search_fields = ("name", "code")



@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "asset_type",
        "area",
        "code",
        "manufacturer",
    )

    list_filter = (
        "asset_type",
        "area",
    )

    search_fields = (
        "name",
        "code",
        "serial_number",
    )