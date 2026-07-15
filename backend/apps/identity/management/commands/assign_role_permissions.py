from django.core.management.base import BaseCommand

from apps.identity.models import Permission, Role, RolePermission

ROLE_PERMISSIONS = {
    "Admin": [
        "*",
    ],
    "Manager": [
        "asset.view",
        "asset.create",
        "asset.update",
        "asset.delete",
        "plant.view",
        "plant.create",
        "plant.update",
        "plant.delete",
        "area.view",
        "area.create",
        "area.update",
        "area.delete",
        "organization.view",
        "organization.create",
        "organization.update",
        "organization.delete",
    ],
    "Operator": [
        "asset.view",
        "asset.create",
        "asset.update",
        "plant.view",
        "plant.create",
        "plant.update",
        "area.view",
        "area.create",
        "area.update",
    ],
    "Viewer": [
        "asset.view",
        "plant.view",
        "area.view",
        "organization.view",
        "user.view",
    ],
}


class Command(BaseCommand):
    help = "Assign permissions to system roles"

    def handle(self, *args, **options):

        for role_name, permission_codes in ROLE_PERMISSIONS.items():

            role = Role.objects.get(name=role_name)

            if "*" in permission_codes:
                permissions = Permission.objects.all()
            else:
                permissions = Permission.objects.filter(code__in=permission_codes)

            for permission in permissions:
                RolePermission.objects.get_or_create(
                    role=role,
                    permission=permission,
                )

        self.stdout.write(self.style.SUCCESS("Role permissions assigned successfully."))
