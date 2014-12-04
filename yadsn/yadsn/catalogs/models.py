"""
Models catalog.
"""

from pybinder import Catalog
from pybinder.decorators import provides

import users.models


class ModelsCatalog(Catalog):

    namespace = 'models'

    @provides('user_manager')
    def provide_user_manager(self):
        """
        :rtype: users.models.UserManager
        """
        return users.models.UserManager()

    @provides('subscription_manager')
    def provide_subscription_manager(self):
        return users.models.SubscriptionManager()


catalog = ModelsCatalog()
