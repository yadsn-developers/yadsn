"""
Database models catalog.
"""

from objects import AbstractCatalog
from objects.providers import Class

from yadsn.models import (
    subscriptions,
)


class Models(AbstractCatalog):
    """
    Models catalog.
    """

    subscriber = Class(subscriptions.Subscriber)
    """ :type: (objects.Provider) -> subscriptions.Subscriber """
