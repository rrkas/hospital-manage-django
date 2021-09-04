from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
