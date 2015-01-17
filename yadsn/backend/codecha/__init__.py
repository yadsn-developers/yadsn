"""
Codecha client.
"""

from objects import Catalog
from objects.providers import NewInstance
from objects.injections import InitArg

from . import client
from django.conf import settings


class Codecha(Catalog):
    """
    Application objects catalog.
    """

    codecha_client = NewInstance(client.CodechaClient,
                                 InitArg('public_key',
                                         settings.CODECHA_KEYS['public_key']),
                                 InitArg('private_key',
                                         settings.CODECHA_KEYS['private_key']))

