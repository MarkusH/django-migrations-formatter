# Changelog

## Under development

- A minimum version of `black>=22.1.0` is required.

- Added the `black` and `isort` installation extras. One can now automatically
  install black and isort with `python -m pip install
  "django-migrations-formatter[black,isort]"`.

## 0.1.5 (2021-10-06)

* Add explicit support for Django 4.0 and Python 3.10

## 0.1.4 (2021-04-06)

* Add explicit support for Django 3.2

## 0.1.3 (2021-04-02)

* Another shot at a single-file GitHub workflow

## 0.1.2 (2021-04-02)

* Fix release building

## 0.1.1 (2021-04-02)

* Use [pre-commit.ci](https://results.pre-commit.ci/repo/github/351587462) for linting

* Use a single workflow file

## 0.1.0 (2021-03-26)

* Initial version. Django Migration files are automatically formatted with
  black and isort of those tools are installed.
