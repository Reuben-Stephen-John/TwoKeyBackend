# Generated by Django 4.2.6 on 2023-11-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileoperations', '0004_alter_seccheck_geo_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesslog',
            name='file_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
