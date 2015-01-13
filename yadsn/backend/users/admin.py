from django.contrib import admin
from .models import Subscriber, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'se_profile')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'codecha_language', 'added_at', 'http_referrer')

