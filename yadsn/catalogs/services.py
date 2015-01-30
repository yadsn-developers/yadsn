"""
Services catalog.
"""

from objects import AbstractCatalog
from objects.providers import Scoped
from objects.injections import InitArg

from .models import Models
from .resources import Resources

from yadsn.backend.services import (
    subscriptions,
    users,
    auth
)


class Services(AbstractCatalog):
    """
    Services catalog.
    """

    subscriptions = Scoped(subscriptions.Service,
                           InitArg('db', Resources.db),
                           InitArg('subscriber_model', Models.subscriber))
    """ :type: (objects.Provider) -> subscriptions.Service """

    users = Scoped(users.Service,
                   InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> users.Service """

    auth = Scoped(auth.Service,
                  InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> users.Service """
