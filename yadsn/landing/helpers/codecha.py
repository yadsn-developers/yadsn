import urllib
import urllib2

class Codecha:
    CODECHA_URL = "http://codecha.org/api/verify"
    RECAPTCHA_URL = "http://www.google.com/recaptcha/api/verify"

    @staticmethod
    def __encode_if_necessary(s):
        if isinstance(s, unicode):
            return s.encode('utf-8')
        return s

    @classmethod
    def __generic_verify(cls, url, challenge, response, remoteip, private_key):
        params = urllib.urlencode({
            'privatekey': cls.__encode_if_necessary(private_key),
            'remoteip':   cls.__encode_if_necessary(remoteip),
            'response':   cls.__encode_if_necessary(response),
            'challenge':  cls.__encode_if_necessary(challenge),
            })

        request = urllib2.Request(
            url=url,
            data=params,
            headers={ "Content-type": "application/x-www-form-urlencoded" })

        http_response = urllib2.urlopen(request)
        response_lines = http_response.read().splitlines()
        http_response.close()

        if (response_lines[0] == "true"):
            return True

        return False

    @classmethod
    def verify(cls, challenge, response, remoteip, private_key):
        return cls.__generic_verify(cls.CODECHA_URL, challenge, response, remoteip, private_key)

    @classmethod
    def verify_recaptcha(cls, challenge, response, remoteip, private_key):
        return cls.__generic_verify(cls.RECAPTCHA_URL, challenge, response, remoteip, private_key)
