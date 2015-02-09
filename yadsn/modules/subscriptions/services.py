"""
Subscriptions services.
"""

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import mapper
from sqlalchemy.orm.exc import NoResultFound

from yadsn.error import BaseError

from .domains import Subscriber
from .tables import subscriptions


class Subscriptions(object):
    """
    Subscriptions service.
    """

    def __init__(self, db):
        """
        Initializer.

        :type db: yadsn.utils.interfaces.DbInterface
        """
        self.db = db
        mapper(Subscriber, subscriptions(db.metadata))

    def subscribe(self, email, codecha_language, http_referrer=None):
        """
        Subscribes someone.

        :type email: str
        :return:
        """
        subscriber = Subscriber(email=email,
                                codecha_language=codecha_language,
                                http_referrer=http_referrer)
        self.db.session.add(subscriber)
        try:
            self.db.session.commit()
        except IntegrityError:
            self.db.session.rollback()
            raise BaseError('Email {} has been already subscribed'.format(email))
        return subscriber

    def unsubscribe(self, email):
        """
        Unsubscribes someone.

        :param email:
        :return:
        """
        try:
            subscriber = self.db.session.query(Subscriber.email == email).one()
        except NoResultFound:
            pass
        else:
            self.db.session.delete(subscriber)
            self.db.session.commit()
