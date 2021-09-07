from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

import hospital_manage.settings as global_settings


def mfg_date_validator(value):
    if value > timezone.now().date():
        raise ValidationError("Invalid date!")
    return value


def expiry_date_validator(value):
    if value <= timezone.now().date():
        raise ValidationError("Invalid date! Medicine expired!")
    return value


class InventoryItem:
    def __init__(self, name, url_name, count):
        self.name = name
        self.url_name = url_name
        self.count = count


class Manufacturer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    address = models.TextField(null=True)
    company_contact = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                global_settings.PHONE_NUMBER_REGEX,
                "Invalid format! Format: +(1-3) (9-13)",
            )
        ],
        help_text="Format: +(1-3) (9-13)",
        unique=True,
    )
    salesman_contact = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                global_settings.PHONE_NUMBER_REGEX,
                "Invalid format! Format: +(1-3) (9-13)",
            )
        ],
        help_text="Format: +(1-3) (9-13)",
        unique=True,
    )
    website = models.URLField(unique=True)

    def get_absolute_url(self):
        return reverse("manufacturer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=120)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.DO_NOTHING,
        related_name='equipment_manufacturer'
    )
    model = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=2, help_text="(per piece)")
    quantity = models.IntegerField()

    def get_absolute_url(self):
        return reverse("equipment-detail", kwargs={"pk": self.pk})


class Medicine(models.Model):
    name = models.CharField(max_length=120)
    batch = models.CharField(max_length=120, null=True)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.DO_NOTHING,
        related_name='medicine_manufacturer'
    )
    price = models.DecimalField(max_digits=20, decimal_places=2, help_text="(per piece)")
    quantity = models.IntegerField(help_text="(strips/ bottles/ units)")
    mfg_date = models.DateField(help_text="Manufacturing Date", validators=[mfg_date_validator])
    expiry_date = models.DateField(help_text="Expiry Date", validators=[expiry_date_validator])

    def get_absolute_url(self):
        return reverse("medicine-detail", kwargs={"pk": self.pk})

    def is_expired(self):
        return self.expiry_date <= timezone.now().date()
