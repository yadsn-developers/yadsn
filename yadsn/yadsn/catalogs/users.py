"""
Users catalog.
"""

from pybinder.catalogs import Catalog
from pybinder.providers import Factory
from pybinder.requires import Requires

import backend.users.forms
import backend.users.models.user
import backend.users.models.auth


class ModelsCatalog(Catalog):
    """
    Models catalog.
    """

    namespace = 'users.models'

    users = Factory(backend.users.models.user.Users)

    subscriptions = Factory(backend.users.models.user.Subscriptions)

    auth = Factory(backend.users.models.auth.Auth)


class FormsCatalog(Catalog):
    """
    Forms catalog.
    """

    namespace = 'users.forms'

    login_form = Factory(backend.users.forms.LoginForm)

    subscription_form = Factory(backend.users.forms.SubscriptionForm)
    subscription_form.dependencies = [
        Requires('codecha_client', from_namespace='codecha')
    ]
