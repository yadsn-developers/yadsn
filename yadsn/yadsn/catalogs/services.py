"""
Services catalog.
"""

from pybinder import Catalog
from pybinder.decorators import factory, requires

import codecha


class ServicesCatalog(Catalog):

    namespace = 'services'

    @factory
    @requires('codecha', from_namespace='settings', with_name='keys')
    def codecha_client(self, keys):
        """
        :rtype: codecha.CodechaClient
        """
        return codecha.CodechaClient(**keys)


catalog = ServicesCatalog()
