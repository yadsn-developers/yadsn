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

    def __init__(self, client_id, scope, client_secret, redirect_uri):
        """
        Constructor.

        :type client_id: str
        :param client_id: StackExchange app ID
        :type scope: str
        :param scope: requested permissions
        :type client_secret: str
        :param client_secret: StackExchange app secret key
        :type key: str
        :type redirect_uri: str
        :param redirect_uri: callback URI
        :return:
        """
        self.client_id = client_id
        self.scope = scope
        self.client_secret = client_secret
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


class StackexchangeClientMock(object):
    """
    Stackexchange client mock.
    """
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
        :type redirect_uri: str
        :param redirect_uri: callback URI
        :return:
        """
        self.client_id = client_id
        self.scope = scope
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def connect(self):
        """
        Prepares the redirect to StackExchange for access grant.

        :rtype: Request
        :return: request for further redirection
        """
        params = {'code': '123456'}
        response = requests.Request('GET', url=self.redirect_uri, params=params).prepare()
        return response

    def get_token(self, code):
        """
        Retrieves StackExchange access token.

        :type code: str
        :param code: authorization code returned by StackExchange
        :rtype: dict
        :return: {'access_token': 'abcd', 'expires': 1234}
        """
        return {'access_token': 'abcd123abcd123abcd123', 'expires': 1234}