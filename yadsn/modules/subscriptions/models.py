"""
Subscriptions models.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from yadsn.catalogs import Resources


class Subscriber(Resources.db().Model):
    __tablename__ = 'subscriber'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    codecha_language = Column(String)
    added_at = Column(DateTime, default=datetime.utcnow)
    http_referrer = Column(String, nullable=True)

    def __init__(self, email, codecha_language, http_referrer=None):
        self.email = email
        self.codecha_language = codecha_language
        self.http_referrer = http_referrer
