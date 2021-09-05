from django.conf import settings as conf_settings
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from hospital_manage import settings as global_settings


class Patient(models.Model):
    image = models.ImageField(default='patient.jpg', null=True)
    name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name="Date of Birth (DOB)")
    gender = models.CharField(
        max_length=8,
        choices=(
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ),
    )
    mobile = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                global_settings.PHONE_NUMBER_REGEX,
                "Invalid format! Format: +(1-3) (9-13)"
            )
        ],
        help_text="Format: +(1-3) (9-13)",
        unique=True,
    )
    email = models.EmailField(unique=True)
    address = models.TextField()
    aadhaar = models.CharField(
        max_length=15,
        help_text="Aadhaar Card Number Ex: xxxx xxxx xxxx",
        validators=[
            RegexValidator(r"[0-9]{4} [0-9]{4} [0-9]{4}", "Invalid aadhaar number!")
        ],
        unique=True,
    )

    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        conf_settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="created_by",
        null=True,
    )
    archived = models.BooleanField(default=False)
    date_archived = models.DateTimeField(null=True)
    archived_by = models.ForeignKey(
        conf_settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="archived_by",
        null=True,
    )

    def get_absolute_url(self):
        return reverse("patient-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Patient {self.pk}: {self.name}"
