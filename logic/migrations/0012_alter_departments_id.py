# Generated by Django 4.2.6 on 2023-10-18 10:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0011_departments_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
