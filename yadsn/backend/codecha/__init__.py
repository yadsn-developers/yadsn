"""
Codecha application.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance
from objects.injections import InitArg

from . import client
from django.conf import settings


class Catalog(AbstractCatalog):
    """
    Application objects catalog.
    """

    codecha_client = NewInstance(client.CodechaClient,
                                 InitArg('public_key',
                                         settings.CODECHA_KEYS['public_key']),
                                 InitArg('private_key',
                                         settings.CODECHA_KEYS['private_key']))
    """ :type: (objects.Provider) -> client.CodechaClient """
