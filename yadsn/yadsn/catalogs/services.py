"""
Services catalog.
"""

from objects import AbstractCatalog
from objects.providers import NewInstance
from objects.injections import InitArg

from backend.codecha.client import CodechaClient
from django.conf import settings


class Catalog(AbstractCatalog):
    """
    Application objects catalog.
    """

    codecha = NewInstance(CodechaClient,
                          InitArg('public_key',
                                  settings.CODECHA_KEYS['public_key']),
                          InitArg('private_key',
                                  settings.CODECHA_KEYS['private_key']))
    """ :type: (objects.Provider) -> CodechaClient """
