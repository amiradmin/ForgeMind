from django.core.management.base import BaseCommand
from django.db import transaction

from apps.identity.models.permission import Permission
from apps.identity.models.role import Role
from apps.identity.models.role_permission import RolePermission

PERMISSIONS = [
    ("View Organizations", "organization.view"),
    ("Create Organizations", "organization.create"),
    ("Update Organizations", "organization.update"),
    ("Delete Organizations", "organization.delete"),
    ("View Plants", "plant.view"),
    ("Create Plants", "plant.create"),
    ("Update Plants", "plant.update"),
    ("Delete Plants", "plant.delete"),
    ("View Areas", "area.view"),
    ("Create Areas", "area.create"),
    ("Update Areas", "area.update"),
    ("Delete Areas", "area.delete"),
    ("View Assets", "asset.view"),
    ("Create Assets", "asset.create"),
    ("Update Assets", "asset.update"),
    ("Delete Assets", "asset.delete"),
    ("Manage Users", "user.manage"),
    ("Manage Roles", "role.manage"),
]


ROLE_PERMISSIONS = {
    "Admin": [
        "organization.view",
        "organization.create",
        "organization.update",
        "organization.delete",
        "plant.view",
        "plant.create",
        "plant.update",
        "plant.delete",
        "area.view",
        "area.create",
        "area.update",
        "area.delete",
        "asset.view",
        "asset.create",
        "asset.update",
        "asset.delete",
        "user.manage",
        "role.manage",
    ],
    "Manager": [
        "organization.view",
        "plant.view",
        "plant.create",
        "plant.update",
        "area.view",
        "area.create",
        "area.update",
        "asset.view",
        "asset.create",
        "asset.update",
    ],
    "Operator": [
        "plant.view",
        "area.view",
        "asset.view",
        "asset.create",
        "asset.update",
    ],
    "Viewer": [
        "organization.view",
        "plant.view",
        "area.view",
        "asset.view",
    ],
}


class Command(BaseCommand):
    help = "Seed default roles and permissions."

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Creating permissions...")

        permissions = {}

        for name, code in PERMISSIONS:
            permission, _ = Permission.objects.get_or_create(
                code=code,
                defaults={
                    "name": name,
                },
            )
            permissions[code] = permission

        self.stdout.write("Creating roles...")

        for role_name, codes in ROLE_PERMISSIONS.items():
            role, _ = Role.objects.get_or_create(
                name=role_name,
            )

            for code in codes:
                RolePermission.objects.get_or_create(
                    role=role,
                    permission=permissions[code],
                )

        self.stdout.write(self.style.SUCCESS("Roles and permissions seeded successfully."))
