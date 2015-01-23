"""
YADSN informational system.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance, ExternalDependency
from objects.injections import InitArg

from sqlalchemy.engine import interfaces
from sqlalchemy.orm.session import Session

from .models import subscriptions
from . import shared


class YADSNDependencies(AbstractCatalog):
    """
    YADSN external dependencies catalog.
    """

    database = ExternalDependency(instance_of=interfaces.Connectable)
    """ :type: (objects.Provider) -> interfaces.Connectable """

    database_session = ExternalDependency(instance_of=Session)
    """ :type: (objects.Provider) -> Session """


class YADSNModels(AbstractCatalog):
    """
    YADSN models catalog.
    """

    subscriptions_manager = NewInstance(subscriptions.SubscriptionsManager,
                                        InitArg('session', YADSNDependencies.database_session))
    """ :type: (objects.Provider) -> subscriptions.SubscriptionsManager """


class YADSN(object):
    """
    YADSN application.
    """

    Base = shared.Base

    @classmethod
    def start(cls):
        """
        Starts application.
        """
        cls.Base.metadata.bind = YADSNDependencies.database()
