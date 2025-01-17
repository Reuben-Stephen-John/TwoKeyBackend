# Generated by Django 4.2.6 on 2024-01-26 09:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("logic", "0010_userinfo_is_active"),
        ("fileoperations", "0020_delete_file_info"),
    ]

    operations = [
        migrations.CreateModel(
            name="File_Info",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("depts", models.ManyToManyField(to="logic.departments")),
                (
                    "file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fileoperations.objects",
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="logic.organizations",
                    ),
                ),
            ],
            options={
                "db_table": "file_info",
            },
        ),
    ]
