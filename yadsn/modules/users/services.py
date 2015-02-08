"""
Users services.
"""

from sqlalchemy.orm import mapper
from sqlalchemy.exc import IntegrityError

from yadsn.error import BaseError


from .domains import User
from .tables import users


class Users(object):
    """
    Users service.
    """

    def __init__(self, db):
        """
        Initializer.

        :type db: flask.ext.sqlalchemy.SQLAlchemy
        :return:
        """
        self.db = db
        mapper(User, users(db.metadata))

    def create(self, email):
        """
        Creates user.

        :type email: str
        :return:
        """
        user = User(email=email)
        self.db.session.add(user)
        try:
            self.db.session.commit()
        except IntegrityError:
            self.db.session.rollback()
            raise BaseError('User {} has been already created'.format(email))
        return user
