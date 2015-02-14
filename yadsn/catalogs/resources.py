"""
Resources catalog.
"""

from objects import AbstractCatalog
from objects.providers import Singleton
from objects.providers import Config
from objects.injections import InitArg

from yadsn.utils import database
from yadsn.utils import codecha


class Resources(AbstractCatalog):
    """
    Resources catalog.
    """

    config = Config()
    """ :type: (objects.providers.Config) """

    database = Singleton(database.Database,
                         InitArg('url', config.SQLALCHEMY_DATABASE_URI))
    """ :type: (objects.Provider) -> database.Database """

    codecha = Singleton(codecha.Client,
                        InitArg('url', config.CODECHA.URL),
                        InitArg('public_key', config.CODECHA.PUBLIC_KEY),
                        InitArg('private_key', config.CODECHA.PRIVATE_KEY))
    """ :type: (objects.Provider) -> codecha.Client """
