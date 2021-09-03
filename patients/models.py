from django.db import models

from django.utils import timezone


class Patient(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    gender = models.CharField(
        max_length=8,
        choices=(
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ),
    )
    date_created = models.DateTimeField(default=timezone.now)
