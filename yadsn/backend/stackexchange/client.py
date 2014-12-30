"""
Stackexchange access client.
"""

import requests
import urlparse

class StackexchangeClient(object):
    """
    Stackexchange client.
    """
    AUTH_URL= 'https://stackexchange.com/oauth'
    TOKEN_URL = 'https://stackexchange.com/oauth/access_token'
    API_URL = 'https://api.stackexchange.com/2.2'

    def __init__(self, client_id, scope, client_secret, key, redirect_uri):
        """
        Constructor.

        :type client_id: str
        :param client_id: StackExchange app ID
        :type scope: str
        :param scope: requested permissions
        :type client_secret: str
        :param client_secret: StackExchange app secret key
        :type key: str
        :param key: StackExchange app public key
        :type redirect_uri: str
        :param redirect_uri: callback URI
        :return:
        """
        self.client_id = client_id
        self.scope = scope
        self.client_secret = client_secret
        self.key = key
        self.redirect_uri = redirect_uri

    def connect(self):
        """
        Prepares the redirect to StackExchange for access grant.

        :rtype: Request
        :return: request for further redirection
        """
        params = {
            'client_id': self.client_id,
            'scope': self.scope,
            'redirect_uri': self.redirect_uri}
        response = requests.Request('GET', url=self.AUTH_URL, params=params).prepare()
        return response

    def get_token(self, code):
        """
        Retrieves StackExchange access token.

        :type code: str
        :param code: authorization code returned by StackExchange
        :rtype: dict
        :return: {'access_token': 'abcd', 'expires': 1234}
        """
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
        return urlparse.parse_qs(api_response.text)

    def get_se_user(self, access_token):
        """
        Retrieves StackExchange user via /me method.

        :type access_token: str
        :param access_token: access token
        :rtype: dict
        :return: StackExchange user
        """
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