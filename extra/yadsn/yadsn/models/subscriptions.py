"""
Subscriptions models.
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound
from yadsn.shared import Base


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

    def subscribe(self, email):
        """
        Subscribes someone.

        :param email:
        :return:
        """
        subscriber = Subscriber(email=email)
        self.session.add(subscriber)
        self.session.commit()
        return subscriber

    def unsubscribe(self, email):
        """
        Unsubscribes someone.

        :param email:
        :return:
        """
        try:
            subscriber = self.session.query(Subscriber.email == email).one()
        except (MultipleResultsFound, NoResultFound):
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
    email = Column(String)

    def __init__(self, email):
        """
        Initializer.

        :param email:
        :return:
        """
        self.email = email
