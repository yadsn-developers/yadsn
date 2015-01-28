"""
Codecha client.
"""


class Client(object):

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
