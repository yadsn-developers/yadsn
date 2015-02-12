"""
Subscriptions services.
"""

from sqlalchemy.exc import IntegrityError

from yadsn.error import BaseError

from .domains import Subscriber
from .tables import subscriptions


class Subscriptions(object):
    """
    Subscriptions service.
    """

    def __init__(self, database):
        """
        Initializer.

        :type database: yadsn.utils.interfaces.DbInterface
        """
        self.database = database
        self.table = subscriptions(database.metadata)

    def subscribe(self, email, codecha_language, http_referrer=None):
        """
        Subscribes someone.

        :type email: str
        :return:
        """
        with self.database.engine.connect() as connection:
            transaction = connection.begin()
            try:
                result = connection.execute(self.table.insert().values(email=email,
                                                                       codecha_language=codecha_language,
                                                                       http_referrer=http_referrer))
                transaction.commit()
            except IntegrityError:
                transaction.rollback()
                raise BaseError('Email {} has been already subscribed'.format(email))
            return self._get_by_id(*result.inserted_primary_key)

    def unsubscribe(self, email):
        """
        Unsubscribes someone.

        :param email:
        :return:
        """
        with self.database.engine.connect() as connection:
            transaction = connection.begin()
            connection.execute(self.table.delete().where(self.table.columns.email == email))
            transaction.commit()

    def _get_by_id(self, id):
        """
        Returns subscriber object by id.

        :param id:
        :return:
        """
        with self.database.engine.connect() as connection:
            result = connection.execute(self.table.select().where(self.table.columns.id == id))
            subscriber = Subscriber()
            for name, value in dict(result.fetchone()).iteritems():
                setattr(subscriber, name, value)
            return subscriber
