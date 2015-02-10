"""
Resources catalog.
"""

from objects import AbstractCatalog
from objects.providers import Singleton, Config
from objects.injections import InitArg, Attribute

from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData

from yadsn.utils.interfaces import DbInterface
from yadsn.utils import codecha


class Resources(AbstractCatalog):
    """
    Resources catalog.
    """

    config = Config()
    """ :type: (objects.providers.Config) """

    # Database
    database_engine = Singleton(create_engine,
                                InitArg('name_or_url', config.SQLALCHEMY_DATABASE_URI))
    """ :type: (objects.Provider) -> sqlalchemy.engine.Engine """

    database_metadata = Singleton(MetaData,
                                  InitArg('bind', database_engine))
    """ :type: (objects.Provider) -> sqlalchemy.MetaData """

    database = Singleton(DbInterface,
                         Attribute('engine', database_engine),
                         Attribute('metadata', database_metadata))
    """ :type: (objects.Provider) -> yadsn.utils.interfaces.DbInterface """

    # Other resources
    codecha = Singleton(codecha.Client,
                        InitArg('url', config.CODECHA.URL),
                        InitArg('public_key', config.CODECHA.PUBLIC_KEY),
                        InitArg('private_key', config.CODECHA.PRIVATE_KEY))
    """ :type: (objects.Provider) -> codecha.Client """
