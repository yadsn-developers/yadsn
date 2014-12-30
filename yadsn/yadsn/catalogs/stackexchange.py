"""
Stackexchange catalog.
"""

from pybinder.catalogs import Catalog
from pybinder.providers import Factory
from pybinder.requires import Requires

import backend.stackexchange.client


class ServicesCatalog(Catalog):
    """
    Services catalog.
    """

    namespace = 'stackexchange'

    se_client = Factory(backend.stackexchange.client.StackexchangeClient)
    se_client.dependencies = [
        Requires('stackexchange_keys', from_namespace='settings')
    ]
    se_client.producer = lambda cls, stackexchange_keys: cls(**stackexchange_keys)
