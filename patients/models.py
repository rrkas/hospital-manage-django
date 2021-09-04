from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django.utils import timezone


class Patient(models.Model):
    image = models.ImageField()
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
    dob = models.DateTimeField()

    archived = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, related_name="created_by"
    )
    archived_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, related_name="archived_by"
    )

    def get_absolute_url(self):
        return reverse("patient-view", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Patient {self.object.id}: {self.name}"
