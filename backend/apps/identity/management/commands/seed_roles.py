from django.core.management.base import BaseCommand

from apps.identity.models import Role

ROLES = [
    ("Admin", "System administrator"),
    ("Manager", "Plant manager"),
    ("Operator", "Plant operator"),
    ("Viewer", "Read-only user"),
]


class Command(BaseCommand):
    help = "Seed system roles"

    def handle(self, *args, **options):

        created = 0

        for name, description in ROLES:

            _, was_created = Role.objects.get_or_create(
                name=name,
                defaults={
                    "description": description,
                },
            )

            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"{created} roles created."))
