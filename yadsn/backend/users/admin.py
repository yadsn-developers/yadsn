from django.contrib import admin
from .models import Subscriber, User, StackExchangeProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'has_se_profile')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'codecha_language', 'added_at', 'http_referrer')

@admin.register(StackExchangeProfile)
class StackexchangeAdmin(admin.ModelAdmin):
    list_display = ('access_token', 'expires', 'reputation')