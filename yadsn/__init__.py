"""
YADSN informational system.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance, Object, ExternalDependency
from objects.injections import InitArg
from sqlalchemy.engine import interfaces
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.scoping import scoped_session

from .models import subscriptions
from . import shared


class Dependencies(AbstractCatalog):
    """
    External dependencies catalog.
    """

    config = ExternalDependency(instance_of=dict)
    """ :type: (objects.Provider) -> dict """

    database = ExternalDependency(instance_of=interfaces.Connectable)
    """ :type: (objects.Provider) -> interfaces.Connectable """

    database_session = ExternalDependency(instance_of=(scoped_session,
                                                       Session))
    """ :type: (objects.Provider) -> Session """


class Services(AbstractCatalog):
    """
    Services catalog.
    """

    codecha = None

    stack_exchange = None


class Models(AbstractCatalog):
    """
    Models catalog.
    """

    subscriptions_manager = NewInstance(subscriptions.SubscriptionsManager,
                                        InitArg('session', Dependencies.database_session))
    """ :type: (objects.Provider) -> subscriptions.SubscriptionsManager """


class YADSN(object):
    """
    YADSN application.
    """

    @classmethod
    def start(cls, database_engine, database_session, config):
        """
        Starts application.
        """
        Dependencies.database.satisfy(Object(database_engine))
        Dependencies.database_session.satisfy(Object(database_session))
        Dependencies.config.satisfy(Object(config))

        shared.Base.metadata.bind = Dependencies.database()
