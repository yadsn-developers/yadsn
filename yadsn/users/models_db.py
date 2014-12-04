"""
Users database models.
"""

from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    codecha_language = models.CharField(max_length=20)
    added_at = models.DateTimeField(auto_now_add=True)
    http_referrer = models.CharField(max_length=255)
