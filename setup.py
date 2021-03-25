import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="django-migrations-formatter",
    author="Markus Holtermann",
    author_email="info@markusholtermann.eu",
    description="A Django library to automatically format your migrations.",
    license="BSD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkusH/django-migrations-formatter",
    project_urls={
        "CI": "https://github.com/MarkusH/django-migrations-formatter/actions",  # noqa
        "Changelog": "https://github.com/MarkusH/django-migrations-formatter/blob/main/CHANGELOG.md",  # noqa
        "Issues": "https://github.com/MarkusH/django-migrations-formatter/issues",  # noqa
    },
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    include_package_data=True,
    extras_require={
        "dev": ["pre-commit"],
        "test": [
            "coverage[toml]>=5,<6",
            "Django",
            "black",
            "isort",
        ],
    },
    setup_requires=["setuptools_scm>=5<6"],
    use_scm_version=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
