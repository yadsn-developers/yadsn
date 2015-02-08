"""

"""

from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime


def users(metadata):
    return Table('user', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('email', String, unique=True),
                 Column('registered_at', DateTime, default=datetime.utcnow))



