# Generated by Django 4.2.6 on 2023-11-09 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0007_userinfo_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logic.userinfo'),
        ),
    ]
