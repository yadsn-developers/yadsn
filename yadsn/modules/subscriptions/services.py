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

    def __init__(self, db, models):
        """
        Initializer.

        :type db: flask.ext.sqlalchemy.SQLAlchemy
        :type models: Catalog
        :return:
        """
        self.db = db
        self.models = models

    def subscribe(self, email, codecha_language, http_referrer=None):
        """
        Subscribes someone.

        :type email: str
        :return:
        """
        subscriber = self.models.Subscriber(email=email,
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
            subscriber = self.db.session.query(self.models.Subscriber.email == email).one()
        except NoResultFound:
            pass
        else:
            self.db.session.delete(subscriber)
            self.db.session.commit()
