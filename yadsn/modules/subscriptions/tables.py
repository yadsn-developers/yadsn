"""
Subscriptions database tables.
"""

from datetime import datetime
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime


def subscriptions(metadata):
    return Table('subscriber', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('email', String, unique=True),
                 Column('codecha_language', String),
                 Column('added_at', DateTime, default=datetime.utcnow),
                 Column('http_referrer', String, nullable=True))
