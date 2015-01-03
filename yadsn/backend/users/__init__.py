"""
Users catalog.
"""

import objects

from backend.codecha import CodechaClient
from .models import user
from .models import auth
from . import forms


@objects.register(user.Users)
class UserManager(objects.Provider):
    pass


@objects.register(user.Subscriptions)
class SubscriptionsManager(objects.Provider):
    pass


@objects.register(auth.Auth)
class AuthManager(objects.Provider):
    pass


@objects.register(forms.LoginForm)
class LoginForm(objects.Provider):
    pass


@objects.register(forms.SubscriptionForm)
@objects.inject(codecha_client=CodechaClient)
class SubscriptionForm(objects.Provider):
    pass
