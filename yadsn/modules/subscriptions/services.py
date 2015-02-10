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
        self.subscribtion_table = subscriptions(database.metadata)

    def subscribe(self, email, codecha_language, http_referrer=None):
        """
        Subscribes someone.

        :type email: str
        :return:
        """
        with self.database.engine.connect() as connection:
            transaction = connection.begin()
            insert = self.subscribtion_table.insert()
            try:
                result = connection.execute(insert.values(email=email,
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
            delete = self.subscribtion_table.delete()
            connection.execute(delete.where(self.subscribtion_table.c.email == email))
            transaction.commit()

    def _get_by_id(self, id):
        """
        Returns subscriber object by id.

        :param id:
        :return:
        """
        with self.database.engine.connect() as connection:
            select = self.subscribtion_table.select()
            result = connection.execute(select.where(self.subscribtion_table.c.id == id))
            subscriber = Subscriber()
            for name, value in dict(result.fetchone()).iteritems():
                setattr(subscriber, name, value)
            return subscriber
