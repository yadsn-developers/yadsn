"""
Subscriptions forms.
"""

from wtforms import Form, StringField, validators


class SubscriptionForm(Form):
    """
    Subscription form.
    """

    email = StringField('Email Address', [validators.Length(min=6, max=35)])
