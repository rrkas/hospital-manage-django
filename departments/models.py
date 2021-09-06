from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbr = models.CharField(max_length=8, unique=True)
    description = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse("department-detail", kwargs={"pk": self.pk})

    def doctor_count(self):
        from doctors.models import Doctor

        return Doctor.objects.filter(pk=self.pk).count()

    def __str__(self):
        return f"{self.name} ({self.abbr})"
