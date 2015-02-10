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

    def __init__(self, database):
        """
        Initializer.

        :type database: yadsn.utils.interfaces.DbInterface
        """
        self.database = database
        mapper(User, users(database.metadata))

    def create(self, email):
        """
        Creates user.

        :type email: str
        :return:
        """
        user = User(email=email)
        self.database.session.add(user)
        try:
            self.database.session.commit()
        except IntegrityError:
            self.database.session.rollback()
            raise BaseError('User {} has been already created'.format(email))
        return user
