"""
Models catalog.
"""

from pybinder import Catalog
from pybinder.decorators import provides

import backend.users.models.user
import backend.users.models.auth


class ModelsCatalog(Catalog):

    namespace = 'models'

    @provides('user_manager')
    def provide_user_manager(self):
        """
        :rtype: users.models.user.UserManager
        """
        return backend.users.models.user.UserManager()

    @provides('subscription_manager')
    def provide_subscription_manager(self):
        """
        :rtype: users.models.user.SubscriptionManager
        """
        return backend.users.models.user.SubscriptionManager()

    @provides('auth_manager')
    def provide_auth_manager(self):
        """
        :rtype: users.models.auth.AuthManager
        """
        return backend.users.models.auth.AuthManager()


catalog = ModelsCatalog()
