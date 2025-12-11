from typing import Any
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create or update a Django superuser from environment variables"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force the creation or update of the admin user even if one exists",
        )

    def handle(self, *args: Any, **options: Any):
        force = options.get("force", False)
        User = get_user_model()

        # If a superuser already exists and we're not forcing, just exit
        superusers = User.objects.filter(is_superuser=True)
        if superusers.exists() and not force:
            self.stdout.write("Superuser(s) already exist. Use --force to override.")
            return

        # Read from environment variables (with defaults)
        admin_username = os.environ.get("DJANGO_ADMIN_USERNAME", "admin")
        admin_password = os.environ.get("DJANGO_ADMIN_PASSWORD")
        admin_email = os.environ.get("DJANGO_ADMIN_EMAIL", "notset@notset.com")

        # Fallback default if no password is provided
        if not admin_password:
            admin_password = "admin"

        # If a user with this username exists and we're forcing, update it
        admin_qs = User.objects.filter(username=admin_username)
        if admin_qs.exists() and force:
            admin_instance = admin_qs.first()
            admin_instance.set_password(admin_password)
            admin_instance.email = admin_email
            admin_instance.is_staff = True
            admin_instance.is_superuser = True
            admin_instance.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully updated admin user '{admin_username}' with new password."
                )
            )
            return

        # Otherwise, create a new superuser
        admin_instance = User.objects.create_superuser(
            username=admin_username,
            email=admin_email,
            password=admin_password,
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created admin user '{admin_username}' "
                f"with password '{admin_password}'"
            )
        )
