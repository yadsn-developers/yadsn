"""
Codecha - developers captcha.
"""

import requests


class CodechaClient(object):
    """
    Codecha client.
    """

    URL = 'https://codecha.org/api/verify'

    def __init__(self, private_key):
        """
        Constructor.

        :param private_key:
        :return:
        """
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
            url=self.URL,
            data={
                'privatekey': self.private_key,
                'remoteip':   remote_ip,
                'response':   response,
                'challenge':  challenge,
            },
            headers={'Content-type': 'application/x-www-form-urlencoded'})

        return api_response.text.strip(' \t\n\r') == 'true'