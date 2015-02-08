"""
Domain models.
"""


class User(object):

    id = None
    email = None
    registered_at = None

    def __init__(self, email=None):
        self.email = email
