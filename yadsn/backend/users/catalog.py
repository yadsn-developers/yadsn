"""
Application catalog.
"""

from pybinder import Catalog
from pybinder.providers import Factory
from pybinder.requires import Requires

from . import forms
from .models import user
from .models import auth


app = Catalog(namespace='users')

# Forms
app.bind('login_form', Factory(forms.LoginForm))

app.bind('subscription_form', Factory(forms.SubscriptionForm, [
    Requires('codecha_client', from_namespace='services')
]))

# Models
app.bind('users', Factory(user.Users))
app.bind('auth', Factory(auth.Auth))
app.bind('subscriptions', Factory(user.Subscriptions))
