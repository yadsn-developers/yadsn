"""
Forms catalog.
"""

from pybinder import Catalog
from pybinder.decorators import factory

import login.forms


class FormsCatalog(Catalog):

    namespace = 'forms'

    @factory
    def login_form(self, *args, **kwargs):
        """
        :rtype: login.forms.LoginForm
        """
        return login.forms.LoginForm(*args, **kwargs)


catalog = FormsCatalog()
