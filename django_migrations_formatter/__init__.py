from django.db.migrations.writer import MigrationWriter

try:
    import black
except ImportError:  # pragma: no cover
    BLACK_INSTALLED = False
else:
    BLACK_INSTALLED = True

try:
    import isort
except ImportError:  # pragma: no cover
    ISORT_INSTALLED = False
else:
    ISORT_INSTALLED = True


def format_black(self, content):
    config_file = black.find_pyproject_toml((self.basedir,))
    if config_file:
        config = black.parse_pyproject_toml(config_file)
    else:
        config = {}
    versions = config.get("target_version", [])
    mode = black.Mode(
        target_versions=[black.TargetVersion[val.upper()] for val in versions],
        line_length=config.get("line_length") or black.Mode.line_length,
        string_normalization=not config.get("skip_string_normalization"),
        experimental_string_processing=bool(
            config.get("experimental_string_processing")
        ),
        is_pyi=bool(config.get("pyi")),
    )
    return black.format_str(content, mode=mode)


def format_isort(self, content):
    return isort.code(content)


def as_string(self):
    content = self._as_string()
    if self._black_installed:
        content = self._format_black(content)
    if self._isort_installed:
        content = self._format_isort(content)
    return content


def patch_migration_writer():
    MigrationWriter._as_string = MigrationWriter.as_string
    MigrationWriter._black_installed = BLACK_INSTALLED
    MigrationWriter._isort_installed = ISORT_INSTALLED
    MigrationWriter._format_black = format_black
    MigrationWriter._format_isort = format_isort
    MigrationWriter.as_string = as_string
