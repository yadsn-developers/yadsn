"""
Users models.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from yadsn.utils.models import ModelsCatalog


class Catalog(ModelsCatalog):
    """
    Models catalog.
    """

    def __init__(self, db):
        """
        Initializer.

        :param db:
        :return:
        """
        class User(db.Model):
            __tablename__ = 'user'

            id = Column(Integer, primary_key=True)
            email = Column(String, unique=True)
            registered_at = Column(DateTime, default=datetime.utcnow)

            def __init__(self, email):
                self.email = email
        self.User = User
