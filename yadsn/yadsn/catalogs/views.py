"""
Views catalog.
"""

from pybinder import Catalog
from pybinder.decorators import factory, requires_provider

import login.views
import landing.views


class ViewsCatalog(Catalog):

    namespace = 'views'

    @factory
    @requires_provider('login_form', from_namespace='forms')
    def login_index(self, login_form):
        """
        :rtype: login.views.Index
        """
        return login.views.Index.as_view(_login_form=login_form)

    @factory
    @requires_provider('codecha_client', from_namespace='services')
    @requires_provider('subscribe_form', from_namespace='forms')
    def landing_index(self, codecha_client, subscribe_form):
        """
        :rtype: landing.views.Index
        """
        return landing.views.Index.as_view(_codecha_client=codecha_client,
                                           _subscribe_form=subscribe_form)


catalog = ViewsCatalog()
