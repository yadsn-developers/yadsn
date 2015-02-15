"""
Subscriptions services.
"""

from sqlalchemy.sql.expression import select
from sqlalchemy.sql.expression import insert
from sqlalchemy.sql.expression import update

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

    def get_by_email(self, email):
        """
        Returns subscriber by email.

        :type email: str
        :rtype: Subscriber
        """
        with self.database.engine.connect() as connection:
            result = connection.execute(select([self.table])
                                        .where(self.table.columns.email == email)).fetchone()
        if not result:
            raise BaseError('Subscriber could not be found by email "{}"'.format(email))
        return Subscriber(**dict(result))

    def get_by_key(self, key):
        """
        Returns subscriber by key.

        :type key: str
        :rtype: Subscriber
        """
        with self.database.engine.connect() as connection:
            result = connection.execute(select([self.table])
                                        .where(self.table.columns.key == key)).fetchone()
        if not result:
            raise BaseError('Subscriber could not be found by key "{}"'.format(key))
        return Subscriber(**dict(result))

    def subscribe(self, email, **kwargs):
        """
        Subscribes someone.

        :type email: str
        :type codecha_language: str
        :type http_referrer: str
        :rtype: Subscriber
        """
        try:
            subscriber = self.get_by_email(email)
        except BaseError:
            with self.database.engine.connect() as connection:
                transaction = connection.begin()
                connection.execute(insert(self.table)
                                   .values(email=email, **kwargs))
                transaction.commit()
            subscriber = self.get_by_email(email)
        else:
            if not subscriber.is_active:
                with self.database.engine.connect() as connection:
                    transaction = connection.begin()
                    connection.execute(update(self.table)
                                       .values(is_active=True)
                                       .where(self.table.columns.id == subscriber.id))
                    transaction.commit()
                subscriber.is_active = True
        return subscriber

    def unsubscribe(self, subscriber):
        """
        Unsubscribes subscriber.

        :type subscriber: Subscriber
        :rtype: None
        """
        with self.database.engine.connect() as connection:
            transaction = connection.begin()
            connection.execute(update(self.table)
                               .values(is_active=False)
                               .where(self.table.columns.id == subscriber.id))
            transaction.commit()
        subscriber.is_active = False
