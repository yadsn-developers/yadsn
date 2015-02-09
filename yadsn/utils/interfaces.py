"""
Interfaces module.
"""


class DbInterface(object):
    session = None
    """
    :type session: sqlalchemy.orm.Session
    """

    metadata = None
    """
    :type session: sqlalchemy.MetaData
    """

    engine = None
    """
    :type engine: sqlalchemy.engine.Engine
    """
