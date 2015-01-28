"""
Codecha client.
"""

import requests


class Client(object):
    """
    Codecha client.
    """

    def __init__(self, url, public_key, private_key):
        """
        Constructor.

        :param url:
        :param public_key:
        :param private_key:
        :return:
        """
        self.url = url
        self.public_key = public_key
        self.private_key = private_key

    def verify(self, challenge, response, remote_ip):
        """
        Verifies challenge response.

        :param challenge:
        :param response:
        :param remote_ip:
        :return:
        """
        if not all((challenge, response, remote_ip)):
            return False

        api_response = requests.post(
            url=self.url,
            data={
                'privatekey': self.private_key,
                'remoteip':   remote_ip,
                'response':   response,
                'challenge':  challenge,
            },
            headers={'Content-type': 'application/x-www-form-urlencoded'})

        return api_response.text.strip('') == 'true'
