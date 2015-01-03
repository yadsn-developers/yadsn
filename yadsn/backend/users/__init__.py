"""
Users catalog.
"""

import objects

from .models import user
from .models import auth
from . import forms


@objects.register('users_manager')
class UserManager(objects.Provider):
    def provide(self):
        return user.Users()


@objects.register('subscriptions_manager')
class SubscriptionsManager(objects.Provider):
    def provide(self):
        return user.Subscriptions()


@objects.register('auth_manager')
class AuthManager(objects.Provider):
    def provide(self):
        return auth.Auth()


@objects.register('login_form')
class LoginForm(objects.Provider):
    def provide(self):
        def login_form_factory(*args, **kwargs):
            return forms.LoginForm(*args, **kwargs)
        return login_form_factory


@objects.register('subscription_form')
class SubscriptionForm(objects.Provider):
    @objects.inject('codecha_client')
    def provide(self, *args, **kwargs):
        return forms.SubscriptionForm(*args, **kwargs)
