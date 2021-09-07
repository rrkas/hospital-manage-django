from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

import hospital_manage.settings as global_settings


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


class Equipment(models.Model):
    name = models.CharField(max_length=120)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    model = models.CharField(max_length=120)
    price = models.FloatField()
    quantity = models.IntegerField()

    def get_absolute_url(self):
        return reverse("equipment-detail", kwargs={"pk": self.pk})
