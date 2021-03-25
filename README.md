# django-migrations-formatter

[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/MarkusH/django-migrations-formatter/Lint%20&%20Test/main?style=for-the-badge)](https://github.com/MarkusH/django-migrations-formatter/actions?query=branch%3Amain+event%3Apush)
[![Codecov branch](https://img.shields.io/codecov/c/gh/MarkusH/django-migrations-formatter/main?style=for-the-badge)](https://app.codecov.io/gh/MarkusH/django-migrations-formatter/branch/main)
[![Version](https://img.shields.io/pypi/v/django-migrations-formatter?label=Version&style=for-the-badge)](https://pypi.org/project/django-migrations-formatter/)
![License](https://img.shields.io/pypi/l/django-migrations-formatter?style=for-the-badge)
![Python Versions](https://img.shields.io/pypi/pyversions/django-migrations-formatter?label=Python&style=for-the-badge)
![Django Versions](https://img.shields.io/pypi/djversions/django-migrations-formatter?color=%230C4B33&label=Django&style=for-the-badge)

This Django library will format Django migrations using
[black](https://pypi.org/project/black/) and [isort](https://pypi.org/project/isort/).

## Installation

Start by installing `django-migrations-formatter` from PyPI:

```console
(env)$ python -m pip install django-migrations-formatter
```

You will also need to make sure to have `black` and/or `isort` installed.
Without them, this library doesn't provide any value.

Then you need to add `django_migrations_formatter.apps.MigrationsFormatter` to
your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    'django_migrations_formatter.apps.MigrationsFormatter',
]
```

## Contributing

The project uses [black](https://pypi.org/project/black/) and
[isort](https://pypi.org/project/isort/) for formatting its code.
[flake8](https://pypi.org/project/flake8/) is used for linting. All these are
combined into [pre-commit](https://pre-commit.com/) to run before each commit
and push. To set it up:

```console
(env)$ python -m pip install '.[dev,test]'
(env)$ pre-commit install -t pre-commit -t pre-push --install-hooks
```

To run the unit tests:

```console
(env)$ django-admin.py test -v 2 --settings=tests.settings
```

If you spot an problem, please [open an issue](https://github.com/MarkusH/django-migrations-formatter/issues/new)
on GitHub.
