"""
User models.
"""

from .database import Subscriber
from django.conf import settings
from backend.users.models import StackExchangeProfile


class Users(object):
    """
    Users model.
    """

    def __init__(self, user):
        """
        Constructor.

        :type user: User
        :param user: User object
        :return:
        """
        self.user = user

    def set_se_token(self, code):
        """
        Saves StackExchange token to a user model.

        :type code: str
        :param code: authorization code returned by StackExchange
        :return:
        """
        se_client = settings.SE_CLIENT_CLS(**settings.STACKEXCHANGE_KEYS)
        token = se_client.get_token(code)
        se_profile = StackExchangeProfile(**token)
        se_profile.save()
        self.user.se_profile = se_profile
        self.user.save()

    def fill_se_profile(self, param):
        """
        Saves StackExchange profile attributes to a user model.

        :type param: list
        :param param: list of attributes
        :return:
        """
        se_client = settings.SE_CLIENT_CLS(**settings.STACKEXCHANGE_KEYS)
        # Todo: manage assumption that a user has a token
        data = se_client.get_se_user_param(access_token=self.user.se_profile.access_token,
                                           param=param)
        self.user.se_profile.fill_profile(**data)
        self.user.se_profile.save()


class Subscriptions(object):
    """
    Subscriptions model.
    """

    def subscribe(self, email, codecha_language=None, http_referrer=None):
        """
        Subscribes user by email.

        :param email:
        :param codecha_language:
        :param http_referrer:
        :return:
        """
        subscriber = Subscriber(email=email,
                                codecha_language=codecha_language,
                                http_referrer=http_referrer)
        subscriber.full_clean()
        subscriber.save()
        return subscriber
