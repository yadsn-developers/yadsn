from django.contrib import admin
from models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'codecha_language', 'added_at', 'http_referrer')