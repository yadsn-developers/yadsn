"""
Services catalog.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance
from objects.injections import InitArg

from .resources import Resources

from yadsn.services import (
    subscriptions,
    users,
    auth
)


class Services(AbstractCatalog):
    """
    Services catalog.
    """

    subscriptions = NewInstance(subscriptions.SubscriptionsService,
                                InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> subscriptions.SubscriptionsManager """

    users = NewInstance(users.UsersService,
                        InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> users.UsersService """

    auth = NewInstance(auth.AuthService,
                       InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> users.UsersService """
