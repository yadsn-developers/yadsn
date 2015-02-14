"""
Interfaces module.
"""

from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine


class Database(object):
    """
    Database client.
    """

    engine = None
    """
    :type engine: sqlalchemy.engine.Engine
    """

    metadata = None
    """
    :type session: sqlalchemy.MetaData
    """

    def __init__(self, url):
        """
        Initializer.

        :type url: str
        :return:
        """
        self.engine = create_engine(url)
        self.metadata = MetaData(bind=self.engine)
