"""
Codecha - developers captcha.
"""

import urllib
import urllib2


class CodechaClient(object):
    """
    Codecha client.
    """

    URL = 'http://codecha.org/api/verify'
    RECAPTCHA_URL = 'http://www.google.com/recaptcha/api/verify'

    def __init__(self, private_key):
        """
        Constructor.

        :param private_key:
        :return:
        """
        self.private_key = private_key

    @staticmethod
    def __encode_if_necessary(s):
        if isinstance(s, unicode):
            return s.encode('utf-8')
        return s

    def _verify(self, url, challenge, response, remote_ip):
        """
        Makes verification.

        :param url:
        :param challenge:
        :param response:
        :param remote_ip:
        :return:
        """
        if not all((challenge, response, remote_ip)):
            return False

        params = urllib.urlencode({
            'privatekey': CodechaClient.__encode_if_necessary(self.private_key),
            'remoteip':   CodechaClient.__encode_if_necessary(remote_ip),
            'response':   CodechaClient.__encode_if_necessary(response),
            'challenge':  CodechaClient.__encode_if_necessary(challenge),
        })

        request = urllib2.Request(
            url=url,
            data=params,
            headers={'Content-type': 'application/x-www-form-urlencoded'})

        http_response = urllib2.urlopen(request)
        response_lines = http_response.read().splitlines()
        http_response.close()

        if response_lines[0] == 'true':
            return True

        return False

    def verify(self, challenge, response, remote_ip):
        """
        Verifies challenge response.

        :param challenge:
        :param response:
        :param remote_ip:
        :return:
        """
        return self._verify(self.URL, challenge, response, remote_ip)

    def verify_recaptcha(self, challenge, response, remote_ip):
        """
        Verifies recaptcha response.

        :param challenge:
        :param response:
        :param remote_ip:
        :return:
        """
        return self._verify(self.RECAPTCHA_URL, challenge, response, remote_ip)
