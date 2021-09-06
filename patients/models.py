from django.conf import settings as conf_settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from hospital_manage import settings as global_settings


def dob_validator(value):
    if value > timezone.now().date():
        raise ValidationError("Invalid DOB!")
    return value


class Patient(models.Model):
    image = models.ImageField(default='patient.jpg', upload_to='patient_pics')
    name = models.CharField(max_length=100)
    dob = models.DateField(
        verbose_name="Date of Birth (DOB)",
        validators=[dob_validator],
    )
    gender = models.CharField(
        max_length=8,
        choices=(
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ),
        default="male"
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
        null=True,
        unique=True,
    )

    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        conf_settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="patient_created_by",
        null=True,
    )
    archived = models.BooleanField(default=False)
    date_archived = models.DateTimeField(null=True)
    archived_by = models.ForeignKey(
        conf_settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="patient_archived_by",
        null=True,
    )

    def get_absolute_url(self):
        return reverse("patient-detail", kwargs={"pk": self.pk})

    def age(self):
        return int((timezone.now().date() - self.dob).days / 365.25)

    def __str__(self):
        return f"Patient {self.pk}: {self.name}"
