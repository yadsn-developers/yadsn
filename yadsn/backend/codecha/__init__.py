import objects

from . import client
from django.conf import settings


class Catalog(objects.Catalog):
    """
    Objects catalog.
    """

    codecha_client = objects.NewInstance(
        provides=client.CodechaClient,
        **settings.CODECHA_KEYS
    )
    """
    :type: (objects.Provider) -> client.CodechaClient
    """
