# Generated by Django 4.2.5 on 2023-09-16 22:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                max_length=50,
                validators=[
                    django.core.validators.MinLengthValidator(
                        limit_value=2,
                        message="Le prénom doit comporter au moins 2 caractères.",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                max_length=50,
                validators=[
                    django.core.validators.MinLengthValidator(
                        limit_value=2,
                        message="Le nom de famille doit comporter au moins 2 caractères.",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=50,
                validators=[
                    django.core.validators.MinLengthValidator(
                        limit_value=3,
                        message="Le nom d'utilisateur doit comporter au moins 3 caractères.",
                    )
                ],
            ),
        ),
    ]
