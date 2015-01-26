"""
Subscriptions service models.
"""

from datetime import datetime
from yadsn.extensions import db


class Subscriber(db.Model):
    """
    Subscriber database model.
    """

    __tablename__ = 'subscriber'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    codecha_language = db.Column(db.String)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    http_referrer = db.Column(db.String, nullable=True)

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
