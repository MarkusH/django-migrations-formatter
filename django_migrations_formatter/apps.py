from django.apps import AppConfig

from . import patch_migration_writer


class MigrationsFormatter(AppConfig):
    name = "django_migrations_formatter"

    def ready(self) -> None:
        patch_migration_writer()
