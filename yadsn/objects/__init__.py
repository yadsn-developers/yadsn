"""
`Objects` library.
"""

from functools import wraps
from inspect import isclass


PROVIDERS = dict()


class Provider(object):

    injections = {}

    def __init__(self, cls):
        self.cls = cls
        self.injections = self.injections.copy()

    def provide(self):
        return self.cls(**dict((
            (name, PROVIDERS[provider].provide())
            for name, provider in self.injections.iteritems()
        )))


def register(cls):
    def decorated(provider):
        PROVIDERS[provider] = provider(cls)
        return provider
    return decorated


# def override(alias):
#     def decorator(provider_cls):
#         PROVIDERS[alias] = provider_cls()
#         return provider_cls
#     return decorator


def inject(**injections):
    def decorator(callback):

        if isclass(callback) and issubclass(callback, Provider):
            callback.injections.update(injections)
            return callback

        @wraps(callback)
        def decorated(*args, **kwargs):
            for name, provider in injections.iteritems():
                if name not in kwargs:
                    kwargs[name] = PROVIDERS[provider].provide()
            return callback(*args, **kwargs)
        return decorated
    return decorator
