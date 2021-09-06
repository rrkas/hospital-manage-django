# Generated by Django 3.2.7 on 2021-09-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
                default="male",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="image",
            field=models.ImageField(
                default="patient.jpg", null=True, upload_to="patient_pics"
            ),
        ),
    ]
