"""
Forms catalog.
"""

from pybinder import Catalog
from pybinder.decorators import provides

import login.forms
import landing.forms


class FormsCatalog(Catalog):

    namespace = 'forms'

    @provides('login_form')
    def provide_login_form(self, *args, **kwargs):
        """
        :rtype: login.forms.LoginForm
        """
        return login.forms.LoginForm(*args, **kwargs)

    @provides('subscribe_form')
    def provide_subscribe_form(self, *args, **kwargs):
        """
        :rtype: landing.forms.SubscribeForm
        """
        return landing.forms.SubscribeForm(*args, **kwargs)


catalog = FormsCatalog()
