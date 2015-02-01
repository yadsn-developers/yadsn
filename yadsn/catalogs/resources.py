"""
Resources catalog.
"""

from objects import AbstractCatalog
from objects.providers import Singleton, Config
from objects.injections import InitArg

from flask.ext.sqlalchemy import SQLAlchemy
from yadsn.utils import codecha


class Resources(AbstractCatalog):
    """
    Resources catalog.
    """

    config = Config()
    """ :type: (objects.providers.Config) """

    db = Singleton(SQLAlchemy)
    """ :type: (objects.Provider) -> SQLAlchemy """

    codecha = Singleton(codecha.Client,
                        InitArg('url', config.CODECHA.URL),
                        InitArg('public_key', config.CODECHA.PUBLIC_KEY),
                        InitArg('private_key', config.CODECHA.PRIVATE_KEY))
    """ :type: (objects.Provider) -> codecha.Client """
