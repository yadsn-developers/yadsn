"""
YADSN informational system.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance, ExternalDependency
from objects.injections import InitArg

from sqlalchemy.orm.session import Session
from sqlalchemy.orm.scoping import scoped_session

from .models import subscriptions


class Dependencies(AbstractCatalog):
    """
    External dependencies catalog.
    """

    config = ExternalDependency(instance_of=dict)
    """ :type: (objects.Provider) -> dict """

    database_session = ExternalDependency(instance_of=(scoped_session,
                                                       Session))
    """ :type: (objects.Provider) -> Session """


class Services(AbstractCatalog):
    """
    Services catalog.
    """

    codecha = None

    stack_exchange = None

    github = None


class Models(AbstractCatalog):
    """
    Models catalog.
    """

    subscriptions_manager = NewInstance(subscriptions.SubscriptionsManager,
                                        InitArg('session', Dependencies.database_session))
    """ :type: (objects.Provider) -> subscriptions.SubscriptionsManager """

    users_manager = None

    auth_manager = None
