"""
Models catalog.
"""

from pybinder import Catalog
from pybinder.decorators import provides

import backend.users.models.user
import backend.users.models.auth


class ModelsCatalog(Catalog):

    namespace = 'models'

    @provides('users')
    def provide_users(self):
        """:rtype: users.models.user.Users"""
        return backend.users.models.user.Users()

    @provides('subscriptions')
    def provide_subscriptions(self):
        """:rtype: users.models.user.Subscriptions"""
        return backend.users.models.user.Subscriptions()

    @provides('auth')
    def provide_auth(self):
        """:rtype: users.models.auth.Auth"""
        return backend.users.models.auth.Auth()


catalog = ModelsCatalog()
