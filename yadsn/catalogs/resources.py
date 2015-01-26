"""
Resources catalog.
"""

from objects import AbstractCatalog
from objects.providers import ExternalDependency

from flask.ext.sqlalchemy import SQLAlchemy


class Resources(AbstractCatalog):
    """
    Resources catalog.
    """

    config = ExternalDependency(instance_of=dict)
    """ :type: (objects.Provider) -> dict """

    db = ExternalDependency(instance_of=SQLAlchemy)
    """ :type: (objects.Provider) -> SQLAlchemy """
