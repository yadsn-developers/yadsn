"""
Users database models.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    codecha_language = models.CharField(max_length=20)
    added_at = models.DateTimeField(auto_now_add=True)
    http_referrer = models.CharField(max_length=255)


class StackExchangeProfile(models.Model):
    access_token = models.CharField(max_length=100)


class User(AbstractUser):
    se_profile = models.OneToOneField(StackExchangeProfile, null=True)