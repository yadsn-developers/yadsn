"""
Subscriptions database tables.
"""

from datetime import datetime
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean


def subscriptions(metadata):
    return Table('subscriber', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('email', String(20), unique=True),
                 Column('key', String(32), unique=True),
                 Column('is_active', Boolean),
                 Column('codecha_language', String(16)),
                 Column('added_at', DateTime, default=datetime.utcnow),
                 Column('http_referrer', String, nullable=True))
