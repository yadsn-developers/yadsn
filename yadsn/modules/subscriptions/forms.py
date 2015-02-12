"""
Subscriptions forms.
"""

from wtforms import Form
from wtforms import StringField
from wtforms import validators


class SubscriptionForm(Form):
    """
    Subscription form.
    """

    email = StringField('Email Address', [validators.Length(min=6, max=35)])
