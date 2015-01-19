"""
Forms catalog.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance
from objects.injections import InitArg

from . import services
from backend.users import forms as users_forms


class Catalog(AbstractCatalog):
    """
    Forms catalog.
    """

    subscription = NewInstance(users_forms.SubscriptionForm,
                               InitArg('codecha_client',
                                       services.Catalog.codecha))
    """ :type: (objects.Provider) -> users_forms.SubscriptionForm """

    login = NewInstance(users_forms.LoginForm)
    """ :type: (objects.Provider) -> users_forms.LoginForm """
