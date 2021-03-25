import datetime
import textwrap
from unittest import mock

from django.db import migrations, models
from django.db.migrations.writer import MigrationWriter
from django.test import SimpleTestCase


class TestMigrationWriter(SimpleTestCase):
    def get_migration(self):
        fields = {
            "charfield": models.DateTimeField(default=datetime.datetime.utcnow),
            "datetimefield": models.DateTimeField(default=datetime.datetime.utcnow),
        }

        options = {
            "verbose_name": "My model",
            "verbose_name_plural": "My models",
        }

        migration = type(
            "Migration",
            (migrations.Migration,),
            {
                "app_label": "django_migrations_formatter",
                "dependencies": [("testapp", "some_other_one")],
                "operations": [
                    migrations.CreateModel(
                        "MyModel", tuple(fields.items()), options, (models.Model,)
                    ),
                    migrations.CreateModel(
                        "MyModel2", tuple(fields.items()), bases=(models.Model,)
                    ),
                    migrations.CreateModel(
                        name="MyModel3",
                        fields=tuple(fields.items()),
                        options=options,
                        bases=(models.Model,),
                    ),
                    migrations.DeleteModel("MyModel"),
                    migrations.AddField(
                        "OtherModel", "datetimefield", fields["datetimefield"]
                    ),
                ],
            },
        )

        return migration

    def assertInOutput(self, expected, output):
        if expected not in output:
            print("Expected this:")
            print(expected)
            print("to be in:")
            print(output)
            self.fail("Failed")

    def test_black_and_isort(self):
        writer = MigrationWriter(self.get_migration())
        output = writer.as_string()
        expected = textwrap.dedent(
            """
                import datetime

                from django.db import migrations, models


                class Migration(migrations.Migration):

                    dependencies = [
                        ("testapp", "some_other_one"),
                    ]

                    operations = [
                        migrations.CreateModel(
                            name="MyModel",
                            fields=[
                                ("charfield", models.DateTimeField(default=datetime.datetime.utcnow)),
                                (
                                    "datetimefield",
                                    models.DateTimeField(default=datetime.datetime.utcnow),
                                ),
                            ],
                            options={
                                "verbose_name": "My model",
                                "verbose_name_plural": "My models",
                            },
                        ),
                        migrations.CreateModel(
                            name="MyModel2",
                            fields=[
                                ("charfield", models.DateTimeField(default=datetime.datetime.utcnow)),
                                (
                                    "datetimefield",
                                    models.DateTimeField(default=datetime.datetime.utcnow),
                                ),
                            ],
                        ),
                        migrations.CreateModel(
                            name="MyModel3",
                            fields=[
                                ("charfield", models.DateTimeField(default=datetime.datetime.utcnow)),
                                (
                                    "datetimefield",
                                    models.DateTimeField(default=datetime.datetime.utcnow),
                                ),
                            ],
                            options={
                                "verbose_name": "My model",
                                "verbose_name_plural": "My models",
                            },
                        ),
                        migrations.DeleteModel(
                            name="MyModel",
                        ),
                        migrations.AddField(
                            model_name="OtherModel",
                            name="datetimefield",
                            field=models.DateTimeField(default=datetime.datetime.utcnow),
                        ),
                    ]
            """  # noqa
        )
        self.assertInOutput(expected, output)

    def test_only_black(self):
        writer = MigrationWriter(self.get_migration())
        writer._isort_installed = False
        with mock.patch(
            "black.parse_pyproject_toml", return_value={"line_length": 100}
        ):
            # We only call `parse_pyproject_toml()` when we found a config file.
            # In that case, we mock the config here to be different to the
            # default one (e.g. 100 vs 88 chars per line)
            output = writer.as_string()
        expected = textwrap.dedent(
            """
                import datetime
                from django.db import migrations, models


                class Migration(migrations.Migration):

                    dependencies = [
                        ("testapp", "some_other_one"),
                    ]

                    operations = [
                        migrations.CreateModel(
                            name="MyModel",
                            fields=[
                                ("charfield", models.DateTimeField(default=datetime.datetime.utcnow)),
                                ("datetimefield", models.DateTimeField(default=datetime.datetime.utcnow)),
                            ],
                            options={
                                "verbose_name": "My model",
                                "verbose_name_plural": "My models",
                            },
                        ),
                        migrations.CreateModel(
                            name="MyModel2",
                            fields=[
                                ("charfield", models.DateTimeField(default=datetime.datetime.utcnow)),
                                ("datetimefield", models.DateTimeField(default=datetime.datetime.utcnow)),
                            ],
                        ),
                        migrations.CreateModel(
                            name="MyModel3",
                            fields=[
                                ("charfield", models.DateTimeField(default=datetime.datetime.utcnow)),
                                ("datetimefield", models.DateTimeField(default=datetime.datetime.utcnow)),
                            ],
                            options={
                                "verbose_name": "My model",
                                "verbose_name_plural": "My models",
                            },
                        ),
                        migrations.DeleteModel(
                            name="MyModel",
                        ),
                        migrations.AddField(
                            model_name="OtherModel",
                            name="datetimefield",
                            field=models.DateTimeField(default=datetime.datetime.utcnow),
                        ),
                    ]
            """  # noqa
        )
        self.assertInOutput(expected, output)

    def test_only_black_without_config(self):
        writer = MigrationWriter(self.get_migration())
        writer._isort_installed = False
        with mock.patch("black.find_pyproject_toml", return_value=None):
            output = writer.as_string()
        expected = textwrap.dedent(
            """
                import datetime
                from django.db import migrations, models


                class Migration(migrations.Migration):

                    dependencies = [
                        ("testapp", "some_other_one"),
                    ]

                    operations = [
                        migrations.CreateModel(
                            name="MyModel",
                            fields=[
                                ("charfield", models.DateTimeField(default=datetime.datetime.utcnow)),
                                (
                                    "datetimefield",
                                    models.DateTimeField(default=datetime.datetime.utcnow),
                                ),
                            ],
                            options={
                                "verbose_name": "My model",
                                "verbose_name_plural": "My models",
                            },
                        ),
                        migrations.CreateModel(
                            name="MyModel2",
                            fields=[
                                ("charfield", models.DateTimeField(default=datetime.datetime.utcnow)),
                                (
                                    "datetimefield",
                                    models.DateTimeField(default=datetime.datetime.utcnow),
                                ),
                            ],
                        ),
                        migrations.CreateModel(
                            name="MyModel3",
                            fields=[
                                ("charfield", models.DateTimeField(default=datetime.datetime.utcnow)),
                                (
                                    "datetimefield",
                                    models.DateTimeField(default=datetime.datetime.utcnow),
                                ),
                            ],
                            options={
                                "verbose_name": "My model",
                                "verbose_name_plural": "My models",
                            },
                        ),
                        migrations.DeleteModel(
                            name="MyModel",
                        ),
                        migrations.AddField(
                            model_name="OtherModel",
                            name="datetimefield",
                            field=models.DateTimeField(default=datetime.datetime.utcnow),
                        ),
                    ]
            """  # noqa
        )
        self.assertInOutput(expected, output)

    def test_only_isort(self):
        writer = MigrationWriter(self.get_migration())
        writer._black_installed = False
        output = writer.as_string()
        expected = textwrap.dedent(
            """
                import datetime

                from django.db import migrations, models


                class Migration(migrations.Migration):

                    dependencies = [
                        ('testapp', 'some_other_one'),
                    ]

                    operations = [
                        migrations.CreateModel(
                            name='MyModel',
                            fields=[
                                ('charfield', models.DateTimeField(default=datetime.datetime.utcnow)),
                                ('datetimefield', models.DateTimeField(default=datetime.datetime.utcnow)),
                            ],
                            options={
                                'verbose_name': 'My model',
                                'verbose_name_plural': 'My models',
                            },
                        ),
                        migrations.CreateModel(
                            name='MyModel2',
                            fields=[
                                ('charfield', models.DateTimeField(default=datetime.datetime.utcnow)),
                                ('datetimefield', models.DateTimeField(default=datetime.datetime.utcnow)),
                            ],
                        ),
                        migrations.CreateModel(
                            name='MyModel3',
                            fields=[
                                ('charfield', models.DateTimeField(default=datetime.datetime.utcnow)),
                                ('datetimefield', models.DateTimeField(default=datetime.datetime.utcnow)),
                            ],
                            options={
                                'verbose_name': 'My model',
                                'verbose_name_plural': 'My models',
                            },
                        ),
                        migrations.DeleteModel(
                            name='MyModel',
                        ),
                        migrations.AddField(
                            model_name='OtherModel',
                            name='datetimefield',
                            field=models.DateTimeField(default=datetime.datetime.utcnow),
                        ),
                    ]
            """  # noqa
        )
        self.assertInOutput(expected, output)

    def test_neither_installed(self):
        writer = MigrationWriter(self.get_migration())
        writer._black_installed = False
        writer._isort_installed = False
        output = writer.as_string()
        expected = textwrap.dedent(
            """
                import datetime
                from django.db import migrations, models


                class Migration(migrations.Migration):

                    dependencies = [
                        ('testapp', 'some_other_one'),
                    ]

                    operations = [
                        migrations.CreateModel(
                            name='MyModel',
                            fields=[
                                ('charfield', models.DateTimeField(default=datetime.datetime.utcnow)),
                                ('datetimefield', models.DateTimeField(default=datetime.datetime.utcnow)),
                            ],
                            options={
                                'verbose_name': 'My model',
                                'verbose_name_plural': 'My models',
                            },
                        ),
                        migrations.CreateModel(
                            name='MyModel2',
                            fields=[
                                ('charfield', models.DateTimeField(default=datetime.datetime.utcnow)),
                                ('datetimefield', models.DateTimeField(default=datetime.datetime.utcnow)),
                            ],
                        ),
                        migrations.CreateModel(
                            name='MyModel3',
                            fields=[
                                ('charfield', models.DateTimeField(default=datetime.datetime.utcnow)),
                                ('datetimefield', models.DateTimeField(default=datetime.datetime.utcnow)),
                            ],
                            options={
                                'verbose_name': 'My model',
                                'verbose_name_plural': 'My models',
                            },
                        ),
                        migrations.DeleteModel(
                            name='MyModel',
                        ),
                        migrations.AddField(
                            model_name='OtherModel',
                            name='datetimefield',
                            field=models.DateTimeField(default=datetime.datetime.utcnow),
                        ),
                    ]
            """  # noqa
        )
        self.assertInOutput(expected, output)
