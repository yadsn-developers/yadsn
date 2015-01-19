"""
Services catalog.
"""

from objects import AbstractCatalog, overrides
from objects.providers import NewInstance
from objects.injections import InitArg

from backend.codecha.client import CodechaClient
from backend.stackexchange.client import StackexchangeClient
from backend.stackexchange.client import StackexchangeClientMock
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

    stack_exchange = NewInstance(StackexchangeClient,
                                 InitArg('client_id',
                                         settings.STACKEXCHANGE_KEYS['client_id']),
                                 InitArg('scope',
                                         settings.STACKEXCHANGE_KEYS['scope']),
                                 InitArg('client_secret',
                                         settings.STACKEXCHANGE_KEYS['client_secret']),
                                 InitArg('key',
                                         settings.STACKEXCHANGE_KEYS['key']),
                                 InitArg('redirect_uri',
                                         settings.STACKEXCHANGE_KEYS['redirect_uri']))
    """ :type: (objects.Provider) -> StackexchangeClient """


if settings.DEBUG:
    @overrides(Catalog)
    class SandboxServices(Catalog):
        stack_exchange = NewInstance(StackexchangeClientMock,
                                     InitArg('client_id',
                                             settings.STACKEXCHANGE_KEYS['client_id']),
                                     InitArg('scope',
                                             settings.STACKEXCHANGE_KEYS['scope']),
                                     InitArg('client_secret',
                                             settings.STACKEXCHANGE_KEYS['client_secret']),
                                     InitArg('key',
                                             settings.STACKEXCHANGE_KEYS['key']),
                                     InitArg('redirect_uri',
                                             settings.STACKEXCHANGE_KEYS['redirect_uri']))
        """ :type: (objects.Provider) -> StackexchangeClient """
