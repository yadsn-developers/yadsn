"""
Application forms.
"""

from objects import AbstractCatalog
# from objects.providers import Singleton, Config
# from objects.injections import InitArg


class Forms(AbstractCatalog):
    """
    Forms catalog.
    """

    config = lambda: None
    """ :type: (objects.Provider) -> None """
