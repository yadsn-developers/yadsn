"""
Subscriptions module.
"""

from objects import AbstractCatalog
from objects.providers import Scoped, ExternalDependency
from objects.injections import InitArg

from flask.ext.sqlalchemy import SQLAlchemy

from . import services
from . import models


class Dependencies(AbstractCatalog):

    db = ExternalDependency(instance_of=SQLAlchemy)
    """ :type: (objects.Provider) -> SQLAlchemy """


class Services(AbstractCatalog):

    subscriptions = Scoped(services.Subscriptions,
                           InitArg('db', Dependencies.db),
                           InitArg('subscriber_model', models.Subscriber))
    """ :type: (objects.Provider) -> subscriptions.Service """


class Forms(AbstractCatalog):

    subscription = None
    """ :type: (objects.Provider) -> subscriptions.Form """


class Subscriptions(object):

    forms = Forms
    services = Services
    dependencies = Dependencies
