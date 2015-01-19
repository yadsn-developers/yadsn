"""
Auth models.
"""
from django.contrib.auth import authenticate, login, logout


class Auth(object):
    """
    Auth model.
    """
    def authenticate(self, username, password):
        user = authenticate(username=username, password=password)
        return user

    def login(self, request, user):
        login(request, user)

    def logout (self, request):
        logout(request)
