"""
Subscriptions models.
"""

from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from yadsn.shared import Base
from yadsn.error import BaseError


class SubscriptionsManager(object):
    """
    Subscriptions manager.
    """

    def __init__(self, session):
        """
        Initializer.

        :param session:
        :return:
        """
        self.session = session

    def subscribe(self, email, codecha_language, http_referrer=None):
        """
        Subscribes someone.

        :param email:
        :return:
        """
        subscriber = Subscriber(email=email,
                                codecha_language=codecha_language,
                                http_referrer=http_referrer)
        self.session.add(subscriber)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise BaseError('Email {} has been already subscribed'.format(email))
        return subscriber

    def unsubscribe(self, email):
        """
        Unsubscribes someone.

        :param email:
        :return:
        """
        try:
            subscriber = self.session.query(Subscriber.email == email).one()
        except NoResultFound:
            pass
        else:
            self.session.delete(subscriber)
            self.session.commit()


class Subscriber(Base):
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
