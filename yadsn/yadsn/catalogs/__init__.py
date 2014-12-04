"""
Application catalogs.
"""

from pybinder import Container, Catalog
from pybinder.providers import Value
from . import forms, models, services

from django.conf import settings


def get_settings_catalog(settings, namespace='settings'):
    catalog = Catalog(namespace=namespace)
    for setting_name in dir(settings):
        if not setting_name.isupper():
            continue
        catalog.bind(setting_name.lower(),
                     Value(getattr(settings, setting_name)))
    return catalog


container = Container(forms.catalog, models.catalog, services.catalog,
                      get_settings_catalog(settings))
container.assemble()

forms = container.namespace('forms')
models = container.namespace('models')

__all__ = ['forms', 'models']
