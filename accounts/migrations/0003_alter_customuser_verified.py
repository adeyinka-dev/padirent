# Generated by Django 5.0.1 on 2024-01-11 22:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_customuser_verified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="verified",
            field=models.BooleanField(default=False),
        ),
    ]
