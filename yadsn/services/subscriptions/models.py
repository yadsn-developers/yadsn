"""
Subscriptions service models.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from yadsn.catalogs import Resources


class Subscriber(Resources.db().Model):
    """
    Subscriber database model.
    """

    __tablename__ = 'subscriber'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    codecha_language = Column(String)
    added_at = Column(DateTime, default=datetime.utcnow)
    http_referrer = Column(String, nullable=True)

    def __init__(self, email, codecha_language, http_referrer=None):
        """
        Initializer.

        :param email:
        :param codecha_language:
        :param http_referrer:
        :return:
        """
        self.email = email
        self.codecha_language = codecha_language
        self.http_referrer = http_referrer
