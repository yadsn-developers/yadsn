"""
Users services.
"""

from sqlalchemy.exc import IntegrityError
from yadsn.error import BaseError


class Users(object):
    """
    Users service.
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

    def create(self, email):
        """
        Creates user.

        :type email: str
        :return:
        """
        user = self.models.User(email=email)
        self.db.session.add(user)
        try:
            self.db.session.commit()
        except IntegrityError:
            self.db.session.rollback()
            raise BaseError('User {} has been already created'.format(email))
        return user
