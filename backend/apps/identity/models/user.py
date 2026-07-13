import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from ..managers import UserManager


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    email = models.EmailField(
        unique=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    job_title = models.CharField(
        max_length=100,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    first_name = models.CharField(
        max_length=150,
        blank=True,
    )

    last_name = models.CharField(
        max_length=150,
        blank=True,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    roles = models.ManyToManyField(
        "identity.Role",
        through="identity.UserRole",
        related_name="users",
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "users"
        ordering = ["email"]

    def __str__(self):
        return self.email

    def has_permission(self, code: str) -> bool:
        """
        Check if user owns a permission through any assigned role.
        """

        return self.roles.filter(
            role_permissions__permission__code=code,
        ).exists()
