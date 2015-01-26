"""
Services catalog.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance
from objects.injections import InitArg

from yadsn.services import (
    subscriptions,
    users,
    auth
)

from .resources import Resources


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
