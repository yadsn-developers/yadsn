"""
Subscriptions domain models.
"""

from yadsn.utils import domain


class Subscriber(domain.Model):
    """
    Subscriber domain model.
    """

    id = None
    email = None
    key = None
    is_active = None
    codecha_language = None
    added_at = None
    http_referrer = None
