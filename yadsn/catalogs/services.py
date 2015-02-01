"""
Application services.
"""

from objects import AbstractCatalog
from objects.providers import Scoped
from objects.injections import InitArg

from .resources import Resources

from yadsn.modules import (
    subscriptions,
    auth,
    users
)


class Services(AbstractCatalog):
    """
    Services catalog.
    """

    subscriptions = Scoped(subscriptions.services.Subscriptions,
                           InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> subscriptions.Service """
