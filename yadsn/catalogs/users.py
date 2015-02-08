"""
Users module catalog.
"""

from objects import AbstractCatalog
from objects.providers import Singleton, NewInstance
from objects.injections import InitArg

from yadsn.modules import users

from .resources import Resources


class Users(AbstractCatalog):
    """
    Users catalog.
    """

    service = Singleton(users.services.Users,
                        InitArg('db', Resources.db))
    """ :type: (objects.Provider) -> users.services.Users """

    login_form = NewInstance(users.forms.LoginForm,
                             InitArg('users_service', service))
    """ :type: (objects.Provider) -> users.forms.LoginForm """

    registration_form = NewInstance(users.forms.RegistrationForm,
                                    InitArg('users_service', service))
    """ :type: (objects.Provider) -> users.forms.RegistrationForm """
