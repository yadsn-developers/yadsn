"""
Domain models.
"""


class Model(object):
    """
    Domain model.
    """

    def __init__(self, **kwargs):
        """
        Initializer.

        :param kwargs:
        :return:
        """
        for name, value in kwargs.iteritems():
            setattr(self, name, value)
        super(Model, self).__init__()
