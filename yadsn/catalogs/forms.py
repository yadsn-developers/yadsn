"""
Forms catalog.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance
from objects.injections import InitArg

from .resources import Resources
from .services import Services

from yadsn.modules import subscriptions, users


class Forms(AbstractCatalog):
    """
    Forms catalog.
    """

    subscriptions = NewInstance(subscriptions.forms.SubscriptionForm,
                                InitArg('codecha', Resources.codecha))
    """ :type: (objects.Provider) -> subscriptions.forms.SubscriptionForm """

    login = NewInstance(users.forms.LoginForm,
                        InitArg('users_service', Services.users))
    """ :type: (objects.Provider) -> users.forms.LoginForm """

    registration = NewInstance(users.forms.RegistrationForm,
                               InitArg('users_service', Services.users))
    """ :type: (objects.Provider) -> users.forms.RegistrationForm """
