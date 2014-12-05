"""
Forms catalog.
"""

from pybinder import Catalog
from pybinder.decorators import provides, requires

import backend.users.forms


class FormsCatalog(Catalog):

    namespace = 'forms'

    @provides('login_form')
    def provide_login_form(self, *args, **kwargs):
        """
        :rtype: backend.users.forms.LoginForm
        """
        return backend.users.forms.LoginForm(*args, **kwargs)

    @provides('subscription_form')
    @requires('codecha_client', from_namespace='services')
    def provide_subscription_form(self, *args, **kwargs):
        """
        :rtype: users.forms.SubscriptionForm
        """
        return backend.users.forms.SubscriptionForm(*args, **kwargs)


catalog = FormsCatalog()
