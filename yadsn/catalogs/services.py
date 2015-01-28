"""
Services catalog.
"""

from objects import AbstractCatalog
from objects.providers import Scoped
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

    subscriptions = Scoped(subscriptions.SubscriptionsService,
                           InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> subscriptions.SubscriptionsService """

    users = Scoped(users.UsersService,
                   InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> users.UsersService """

    auth = Scoped(auth.AuthService,
                  InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> users.UsersService """
