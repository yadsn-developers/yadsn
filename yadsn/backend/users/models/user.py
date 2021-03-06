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

    def __init__(self):
        """
        Constructor.

        :type user: User
        :param user: User object
        :return:
        """
        self.se_client = settings.SE_CLIENT_CLS(**settings.STACKEXCHANGE_KEYS)

    def set_se_token(self, user, code):
        """
        Saves StackExchange token to a user model.

        :type code: str
        :param code: authorization code returned by StackExchange
        :return:
        """
        token = self.se_client.get_token(code)
        se_profile = StackExchangeProfile(**token)
        se_profile.save()
        user.se_profile = se_profile
        user.save()

    def fill_se_profile(self, user, params):
        """
        Saves StackExchange profile attributes to a user model.

        :type params: list
        :param params: list of attributes
        :return:
        """
        # Todo: manage assumption that user has a token
        data = self.se_client.get_user_param(access_token=user.se_profile.access_token,
                                           params=params)
        user.se_profile.fill_profile(**data)
        user.se_profile.save()


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
