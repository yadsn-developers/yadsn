"""
Users application.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance, Singleton
from objects.injections import InitArg

from backend import codecha

from .models import user
from .models import auth
from . import forms


class Catalog(AbstractCatalog):
    """
    Application objects catalog.
    """

    # Forms
    subscription_form = NewInstance(forms.SubscriptionForm,
                                    InitArg('codecha_client',
                                            codecha.Catalog.codecha_client))
    """ :type: (objects.Provider) -> forms.SubscriptionForm """

    login_form = NewInstance(forms.LoginForm)
    """ :type: (objects.Provider) -> forms.LoginForm """

    # Models
    users_model = Singleton(user.Users)
    """ :type: (objects.Provider) -> user.Users """

    auth_model = Singleton(auth.Auth)
    """ :type: (objects.Provider) -> auth.Auth """

    subscriptions_model = Singleton(user.Subscriptions)
    """ :type: (objects.Provider) -> user.Subscriptions """
