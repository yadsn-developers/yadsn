"""
Services catalog.
"""

from pybinder import Catalog
from pybinder.decorators import factory, requires

import codecha


class ServicesCatalog(Catalog):

    namespace = 'services'

    @factory
    @requires('codecha_keys', from_namespace='settings')
    def codecha_client(self, codecha_keys):
        """
        :rtype: codecha.CodechaClient
        """
        return codecha.CodechaClient(codecha_keys['public_key'],
                                     codecha_keys['private_key'])


catalog = ServicesCatalog()
