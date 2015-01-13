from .database import StackExchangeProfile
import requests


class StackExchangeManager(object):

    API_URL = 'https://api.stackexchange.com/2.2'

    def __init__(self, key):
        self.key = key

    def set_token(self, user, token):
        user.se_profile = StackExchangeProfile(**token)
        user.save()

    def get_se_user(self, user):
        """
        Retrieves StackExchange user via /me method.

        :type user: User
        :param user: user
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
                  'access_token': user.se_profile.access_token,
                  'filter': 'default',
                  })
        return api_response.json()


class StackExchangeManagerMock(object):

    API_URL = 'https://api.stackexchange.com/2.2'

    def __init__(self, key):
        self.key = key

    def set_token(self, user, token):
        user.se_profile = StackExchangeProfile(**token)
        user.save()

    def get_se_user(self, user):
        """
        Retrieves StackExchange user via /me method.

        :type user: User
        :param user: user
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