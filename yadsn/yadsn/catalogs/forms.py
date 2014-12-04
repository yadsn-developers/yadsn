"""
Forms catalog.
"""

from pybinder import Catalog
from pybinder.decorators import provides, requires

import login.forms
import users.forms


class FormsCatalog(Catalog):

    namespace = 'forms'

    @provides('login_form')
    def provide_login_form(self, *args, **kwargs):
        """
        :rtype: login.forms.LoginForm
        """
        return login.forms.LoginForm(*args, **kwargs)

    @provides('subscription_form')
    @requires('codecha_client', from_namespace='services')
    def provide_subscribe_form(self, *args, **kwargs):
        """
        :rtype: users.forms.SubscriptionForm
        """
        return users.forms.SubscriptionForm(*args, **kwargs)


catalog = FormsCatalog()
