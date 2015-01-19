"""
User forms.
"""

from django import forms
from backend.users.models import auth


class SubscriptionForm(forms.Form):
    email = forms.EmailField(required=True)
    codecha_language = forms.CharField(required=True,
                                       max_length=32,
                                       widget=forms.HiddenInput())
    http_referrer = forms.CharField(required=True,
                                    max_length=255,
                                    widget=forms.HiddenInput())
    codecha_challenge_field = forms.CharField(required=True,
                                              max_length=128,
                                              widget=forms.HiddenInput())
    codecha_response_field = forms.CharField(required=True,
                                             max_length=128,
                                             widget=forms.HiddenInput())
    client_ip = forms.IPAddressField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        self.codecha_client = kwargs.pop('codecha_client')
        super(SubscriptionForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(SubscriptionForm, self).clean()

        try:
            result = self.codecha_client.verify(
                cleaned_data.pop('codecha_challenge_field'),
                cleaned_data.pop('codecha_response_field'),
                cleaned_data.pop('client_ip'))
        except KeyError:
            raise forms.ValidationError('Please solve Codecha')

        if not result:
            raise forms.ValidationError('Please solve Codecha')

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        user = auth.authenticate(**cleaned_data)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid login credentials")
        return cleaned_data
