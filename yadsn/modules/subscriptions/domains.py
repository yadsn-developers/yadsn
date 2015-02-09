"""
Subscriptions domain models.
"""


class Subscriber(object):

    id = None
    email = None
    codecha_language = None
    added_at = None
    http_referrer = None

    def __init__(self, email=None, codecha_language=None, http_referrer=None):
        self.email = email
        self.codecha_language = codecha_language
        self.http_referrer = http_referrer
