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

    subscriptions = Singleton(subscriptions.services.Subscriptions,
                              InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> subscriptions.services.Subscriptions """

    users = Singleton(users.services.Users,
                      InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> users.services.Users """
