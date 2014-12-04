"""
Forms module.
"""
from django import forms
from .models import Subscriber


class SubscribeForm(forms.Form):
    email = forms.EmailField(required=True)

    def subscribe(self, request):
        email = self.cleaned_data.get('email')
        subscriber = Subscriber(email=email,
                                codecha_language=request.POST.get('codecha_language'),
                                http_referrer=request.META.get('HTTP_REFERER'))
        return subscriber
