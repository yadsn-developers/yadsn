"""
Stackexchange access client.
"""

import requests
from django.shortcuts import redirect

class StackexchangeClient(object):
    """
    Stackexchange client.
    """
    AUTH_URL= 'https://stackexchange.com/oauth'
    TOKEN_URL = 'https://stackexchange.com/oauth/access_token'
    API_URL = 'https://api.stackexchange.com/2.2'

    def __init__(self, client_id, scope, client_secret, key, redirect_uri):
        self.client_id = client_id
        self.scope = scope
        self.client_secret = client_secret
        self.key = key
        self.redirect_uri = redirect_uri

    def connect(self):
        params = {
            'client_id': self.client_id,
            'scope': self.scope,
            'redirect_uri': self.redirect_uri}
        response = requests.Request('GET', url=self.AUTH_URL, params=params).prepare()
        return response

    def get_token(self, code):
        api_response = requests.post(
            url=self.TOKEN_URL,
            data={
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'code': code,
                'redirect_uri': self.redirect_uri,
            },
            headers={'Content-type': 'application/x-www-form-urlencoded'}
        )
        print api_response.text
        return api_response

# https://api.stackexchange.com/2.2/me?key=U4DMV*8nvpm3EOpvf69Rxw((&site=stackoverflow&order=desc&sort=reputation&access_token=b3rbZN0JEXQRqDPnGBJnuA))&filter=default

    def get_se_user(self, access_token):
        url = self.API_URL + '/me'
        api_response = requests.get(
            url=url,
            data={'key': self.key,
                  'site': 'stackoverflow',
                  'order': 'desc',
                  'sort': 'reputation',
                  'access_token': access_token,
                  'filter': 'default',
                  })
        return api_response.json()
