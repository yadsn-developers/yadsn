"""
Forms catalog.
"""

from pybinder import Catalog
from pybinder.decorators import factory

import login.forms
import landing.forms


class FormsCatalog(Catalog):

    namespace = 'forms'

    @factory
    def login_form(self, *args, **kwargs):
        """
        :rtype: login.forms.LoginForm
        """
        return login.forms.LoginForm(*args, **kwargs)

    @factory
    def subscribe_form(self, *args, **kwargs):
        return landing.forms.SubscribeForm(*args, **kwargs)


catalog = FormsCatalog()
