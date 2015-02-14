"""
Services catalog.
"""

from objects import AbstractCatalog
from objects.providers import Singleton
from objects.injections import InitArg

from .resources import Resources

from yadsn.modules import subscriptions, users


class Services(AbstractCatalog):
    """
    Services catalog.
    """

    subscribers = Singleton(subscriptions.services.Subscribers,
                            InitArg('database', Resources.database))
    """ :type: (objects.Provider) -> subscriptions.services.Subscribers """

    users = Singleton(users.services.Users,
                      InitArg('database', Resources.database))
    """ :type: (objects.Provider) -> users.services.Users """
