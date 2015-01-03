
from functools import wraps

PROVIDERS = dict()


def register(alias):
    def decorator(provider_cls):
        PROVIDERS[alias] = provider_cls()
        return provider_cls
    return decorator


def override(alias):
    def decorator(provider_cls):
        PROVIDERS[alias] = provider_cls()
        return provider_cls
    return decorator


def inject(alias, like=None):
    if not like:
        like = alias

    def decorator(callback):
        @wraps(callback)
        def decorated(*args, **kwargs):
            if like not in kwargs:
                kwargs[like] = PROVIDERS[alias].provide()
            return callback(*args, **kwargs)
        return decorated
    return decorator


class Provider(object):

    def provide(self):
        raise NotImplementedError()

    def provider(self):
        return lambda *args, **kwargs: self.provide(*args, **kwargs)
