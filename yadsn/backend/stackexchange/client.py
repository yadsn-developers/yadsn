"""
Stackexchange access.
"""

from requests import Request
from django.shortcuts import redirect

class StackexchangeClient(object):
    """
    Stackexchange client.
    """
    AUTH_URL= 'https://stackexchange.com/oauth'
    TOKEN_URL = 'https://stackexchange.com/oauth/access_token'
    REDIRECT_URI = 'http://yadsn.com'

    def __init__(self, client_id, client_secret, key):
        self.client_id = client_id
        self.client_secret = client_secret
        self.key = key

    def connect(self):
        params = {
            'client_id': self.client_id,
            'scope': '',
            'redirect_uri': self.REDIRECT_URI}
        response = Request('GET', url=self.AUTH_URL, params=params).prepare()
        return redirect(response.url)

    def get_token(self):
        pass

    def get_user(self):
        pass