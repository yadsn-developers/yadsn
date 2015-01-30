"""
Subscriptions services.
"""

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from yadsn.error import BaseError


class Subscriptions(object):
    """
    Subscriptions service.
    """

    def __init__(self, db, subscriber_model):
        """
        Initializer.

        :param db:
        :param subscriber_model:
        :return:
        """
        self.db = db
        self.subscriber_model = subscriber_model

    def subscribe(self, email, codecha_language, http_referrer=None):
        """
        Subscribes someone.

        :param email:
        :return:
        """
        subscriber = self.subscriber_model(email=email,
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
            subscriber = self.db.session.query(self.subscriber_model.email == email).one()
        except NoResultFound:
            pass
        else:
            self.db.session.delete(subscriber)
            self.db.session.commit()
