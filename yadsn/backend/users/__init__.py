"""
Users catalog.
"""

import objects

from .models import user
from .models import auth
from . import forms

from backend import codecha


class Catalog(objects.Catalog):
    """
    Objects catalog.
    """

    users_manager = objects.Singleton(provides=user.Users)
    """
    :type: (objects.Provider) -> user.Users
    """

    subscriptions_manager = objects.Singleton(provides=user.Subscriptions)
    """
    :type: (objects.Provider) -> user.Subscriptions
    """

    auth_manager = objects.Singleton(provides=auth.Auth)
    """
    :type: (objects.Provider) -> auth.Auth
    """

    login_form = objects.NewInstance(provides=forms.LoginForm)
    """
    :type: (objects.Provider) -> forms.LoginForm
    """

    subscriptions_form = objects.NewInstance(
        provides=forms.SubscriptionForm,
        codecha_client=codecha.Catalog.codecha_client
    )
    """
    :type: (objects.Provider) -> forms.SubscriptionForm
    """
