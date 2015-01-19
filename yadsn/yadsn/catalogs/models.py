"""
Models catalog.
"""

from objects import AbstractCatalog
from objects.providers import Singleton
from objects.injections import InitArg

from . import services
from backend.users.models import user
from backend.users.models import auth


class Catalog(AbstractCatalog):
    """
    Models catalog.
    """

    users = Singleton(user.Users,
                      InitArg('stack_exchange',
                              services.Catalog.stack_exchange))
    """ :type: (objects.Provider) -> user.Users """

    auth = Singleton(auth.Auth)
    """ :type: (objects.Provider) -> auth.Auth """

    subscriptions = Singleton(user.Subscriptions)
    """ :type: (objects.Provider) -> user.Subscriptions """
