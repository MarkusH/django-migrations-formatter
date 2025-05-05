from django.db.migrations.writer import MigrationWriter


import subprocess


def as_string(self):
    content = self._as_string()
    fixed = subprocess.check_output(
        ["ruff", "check", "--fix", "-"],
        input=content,
        encoding="utf-8",
    )
    formatted = subprocess.check_output(
        ["ruff", "format", "-"],
        input=fixed,
        encoding="utf-8",
    )

    return formatted


def patch_migration_writer():
    MigrationWriter._as_string = MigrationWriter.as_string
    MigrationWriter.as_string = as_string
