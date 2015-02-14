"""
Subscriptions services.
"""

from sqlalchemy.sql.expression import select
from sqlalchemy.sql.expression import insert
from sqlalchemy.sql.expression import update
from sqlalchemy.exc import IntegrityError

from yadsn.error import BaseError

from .domains import Subscriber
from .tables import subscriptions


class Subscribers(object):
    """
    Subscribers service.
    """

    def __init__(self, database):
        """
        Initializer.

        :type database: yadsn.utils.interfaces.DbInterface
        """
        self.database = database
        self.table = subscriptions(database.metadata)

    def get_by_id(self, id):
        """
        Returns subscriber by id.

        :type id: int
        :rtype: Subscriber
        """
        with self.database.engine.connect() as connection:
            result = connection.execute(select([self.table])
                                        .where(self.table.columns.id == id)).fetchone()
        if not result:
            raise BaseError('Subscriber could not be found by id "{}"'.format(id))
        subscriber = Subscriber()
        for name, value in dict(result).iteritems():
            setattr(subscriber, name, value)
        return subscriber

    def get_by_email(self, email):
        """
        Returns subscriber by email.

        :type email: str
        :rtype: Subscriber
        """
        with self.database.engine.connect() as connection:
            id = connection.execute(select([self.table.columns.id])
                                    .where(self.table.columns.email == email)).scalar()
        if not id:
            raise BaseError('Subscriber could not be found by email "{}"'.format(email))
        return self.get_by_id(id)

    def get_by_key(self, key):
        """
        Returns subscriber by key.

        :type key: str
        :rtype: Subscriber
        """
        with self.database.engine.connect() as connection:
            id = connection.execute(select([self.table.columns.id])
                                    .where(self.table.columns.key == key)).scalar()
        if not id:
            raise BaseError('Subscriber could not be found by key "{}"'.format(key))
        return self.get_by_id(id)

    def subscribe(self, email, codecha_language, http_referrer=None):
        """
        Subscribes someone.

        :type email: str
        :rtype: Subscriber
        """
        with self.database.engine.connect() as connection:
            transaction = connection.begin()
            try:
                result = connection.execute(insert(self.table)
                                            .values(email=email,
                                                    codecha_language=codecha_language,
                                                    http_referrer=http_referrer))
                transaction.commit()
            except IntegrityError:
                transaction.rollback()
                raise BaseError('Email {} has been already subscribed'.format(email))
        return self.get_by_id(*result.inserted_primary_key)

    def unsubscribe(self, subscriber):
        """
        Unsubscribes subscriber.

        :type subscriber: Subscriber
        :rtype: None
        """
        with self.database.engine.connect() as connection:
            transaction = connection.begin()
            connection.execute(update(self.table)
                               .values(is_active=True)
                               .where(self.table.columns.id == subscriber.id))
            transaction.commit()
