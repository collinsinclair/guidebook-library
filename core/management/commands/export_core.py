import os
from datetime import datetime

from django.core.management import call_command, CommandError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Export data from core app with date-based filename"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Overwrite existing file if it exists",
        )

    def handle(self, *args, **options):
        export_dir = "export"
        os.makedirs(export_dir, exist_ok=True)
        today = datetime.now().strftime("%Y%m%d")
        filename = f"{today}.json"
        filepath = os.path.join(export_dir, filename)
        if os.path.exists(filepath):
            if options["force"]:
                self.stdout.write(
                    self.style.WARNING(f"Overwriting existing file {filepath}")
                )
            else:
                raise CommandError(
                    f"File {filepath} already exists. Use --force to overwrite."
                )
        with open(filepath, "w") as f:
            call_command("dumpdata", "core", stdout=f)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully exported core data to {filepath}")
        )
