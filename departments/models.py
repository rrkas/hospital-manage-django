from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbr = models.CharField(max_length=8, unique=True)
    description = models.TextField()
