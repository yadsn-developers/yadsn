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
    expires = models.IntegerField()
    reputation = models.IntegerField(null=True)
    link = models.URLField(null=True)

    def fill_profile(self, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)


class User(AbstractUser):
    se_profile = models.OneToOneField(StackExchangeProfile, null=True, blank=True)

    def has_se_profile(self):
        return bool(self.se_profile)