"""
User models.
"""

from .database import Subscriber


class UserManager(object):
    """
    User manager.
    """


class SubscriptionManager(object):
    """
    Subscription manager.
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
