# Generated by Django 3.2.7 on 2021-09-05 16:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0003_alter_patient_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="aadhaar",
            field=models.CharField(
                blank=True,
                help_text="Aadhaar Card Number Ex: xxxx xxxx xxxx",
                max_length=15,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "[0-9]{4} [0-9]{4} [0-9]{4}", "Invalid aadhaar number!"
                    )
                ],
            ),
        ),
    ]
