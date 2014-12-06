"""
Codecha catalog.
"""

from pybinder.catalogs import Catalog
from pybinder.providers import Factory
from pybinder.requires import Requires

import backend.codecha.client


class ServicesCatalog(Catalog):
    """
    Services catalog.
    """

    namespace = 'codecha'

    codecha_client = Factory(backend.codecha.client.CodechaClient)
    codecha_client.dependencies = [
        Requires('codecha_keys', from_namespace='settings')
    ]
    codecha_client.producer = lambda cls, codecha_keys: cls(**codecha_keys)
