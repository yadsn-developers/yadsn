import objects

from . import client
from django.conf import settings


@objects.register(client.CodechaClient)
class CodechaClient(objects.Provider):
    def provide(self):
        return self.cls(**settings.CODECHA_KEYS)
