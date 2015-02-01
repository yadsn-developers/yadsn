"""
Users forms.
"""


class LoginForm(object):
    """
    Login form.
    """

    def __init__(self, users_service):
        self.users_service = users_service


class RegistrationForm(object):
    """
    Registration form.
    """

    def __init__(self, users_service):
        self.users_service = users_service
