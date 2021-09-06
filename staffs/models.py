from PIL import Image
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import RegexValidator
from django.db import models

import hospital_manage.settings as global_settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(
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
    role = models.CharField(
        max_length=20,
        choices=(
            ("super_admin", "Super Admin"),
            ("admin", "Admin"),
            ("accountant", "Accountant"),
            ("user", "User"),
        ),
        default="user",
    )
    image = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)
