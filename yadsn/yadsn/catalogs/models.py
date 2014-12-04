"""
Models catalog.
"""

from pybinder import Catalog
from pybinder.decorators import provides

import users.models.user
import users.models.auth


class ModelsCatalog(Catalog):

    namespace = 'models'

    @provides('user_manager')
    def provide_user_manager(self):
        """
        :rtype: users.models.UserManager
        """
        return users.models.user.UserManager()

    @provides('subscription_manager')
    def provide_subscription_manager(self):
        return users.models.user.SubscriptionManager()

    @provides('auth_manager')
    def provide_auth_manager(self):
        return users.models.auth.AuthManager


catalog = ModelsCatalog()
