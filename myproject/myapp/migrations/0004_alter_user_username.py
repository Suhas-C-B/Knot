# Generated by Django 5.0.6 on 2024-07-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_user_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
