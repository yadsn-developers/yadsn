"""
Subscriptions module catalog.
"""

from objects import AbstractCatalog
from objects.providers import Singleton, NewInstance
from objects.injections import InitArg

from yadsn.modules import subscriptions

from .resources import Resources


class Subscriptions(AbstractCatalog):
    """
    Subscriptions catalog.
    """

    service = Singleton(subscriptions.services.Subscriptions,
                        InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> subscriptions.services.Subscriptions """

    form = NewInstance(subscriptions.forms.SubscriptionForm)
    """ :type: (objects.Provider) -> subscriptions.forms.SubscriptionForm """
