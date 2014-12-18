"""
Auth models.
"""
from django.contrib.auth import authenticate

class Auth(object):
    """
    Auth model.
    """

    def login(self, username, password):
         user = authenticate(username=username, password=password)
         return user