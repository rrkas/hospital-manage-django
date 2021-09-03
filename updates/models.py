from django.db import models
from django.utils import timezone


class NewsUpdate(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    details = models.TextField()
