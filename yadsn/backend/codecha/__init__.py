import objects

from . import client
from django.conf import settings


@objects.register('codecha_client')
class CodechaClient(objects.Provider):
    def provide(self):
        return client.CodechaClient(**settings.CODECHA_KEYS)
