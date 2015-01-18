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

    def __get_user_dict(self, access_token):
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

    def get_user_param(self, access_token, params):
        """
        Returns a dictionary of Stackexchange user attributes.

        :type access_token: str
        :param access_token: access token
        :type params: list
        :param params: list of attributes
        :rtype: dict
        :return: StackExchange user attributes
        """
        user = self.__get_user_dict(access_token)
        result = dict()
        for key in params:
            result[key] = user['items'][0][key]
        return result


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

    def __get_user_dict(self, access_token):
        """
        Retrieves StackExchange user via /me method.

        :type access_token: str
        :param access_token: access token
        :rtype: dict
        :return: StackExchange user
        """
        return {u'has_more': False,
                u'items': [{u'is_employee': False,
                            u'reputation_change_quarter': 11,
                            u'user_id': 4224439,
                            u'account_id': 5292206,
                            u'reputation_change_month': 7,
                            u'last_modified_date': 1418828763,
                            u'profile_image': u'https://www.gravatar.com/avatar/04998600a315ed8a2da4f8088a2f96dd?s=128&d=identicon&r=PG&f=1',
                            u'user_type': u'registered',
                            u'creation_date': 1415304566,
                            u'last_access_date': 1419926200,
                            u'reputation': 112,
                            u'link': u'http://stackoverflow.com/users/4224439/vadim-tikanov',
                            u'reputation_change_week': 7,
                            u'display_name': u'Vadim Tikanov TEST',
                            u'badge_counts': {u'gold': 0,
                                              u'silver': 0,
                                              u'bronze': 6},
                            u'reputation_change_year': 11,
                            u'reputation_change_day': 0}],
                u'quota_max': 10000, u'quota_remaining': 9999}

    def get_user_param(self, access_token, params):
        """
        Returns a dictionary of Stackexchange user attributes.

        :type access_token: str
        :param access_token: access token
        :type params: list
        :param params: list of attributes
        :rtype: dict
        :return: StackExchange user attributes
        """
        user = self.__get_user_dict(access_token)
        result = dict()
        for key in params:
            result[key] = user['items'][0][key]
        return result