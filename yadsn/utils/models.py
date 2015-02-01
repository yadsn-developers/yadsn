"""
Models utils.
"""


class ModelsCatalog(object):
    """
    Models catalog.
    """

    def __getattr__(self, item):
        """
        Fake getattr.

        :param item:
        :return:
        """
        return getattr(self, item)
