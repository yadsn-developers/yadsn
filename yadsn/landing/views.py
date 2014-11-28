from django.shortcuts import render
from django import forms
from django.core.exceptions import ValidationError
from django.conf import settings
from codecha import CodechaClient
from models import Subscriber
from django.views.generic import View
from django.http import HttpResponse
from django.forms.util import ErrorList


LANDING_TEMPLATE = 'index.html'


class SubscribeForm(forms.Form):
    email = forms.EmailField(required=True)

    def subscribe(self, request):
        email = self.cleaned_data.get('email')
        subscriber = Subscriber(email=email,
                                codecha_language=request.POST.get('codecha_language'),
                                http_referrer=request.META.get('HTTP_REFERER'))
        return subscriber


class Index(View):
    def get(self, request):
        """
        Landing index page.

        :param request:
        :return:
        """
        return render(request,
                      LANDING_TEMPLATE,
                      {'codecha_key': settings.CODECHA_PUBLIC_KEY,
                       'form': SubscribeForm()})

    def post(self, request):
        """
        Landing subscribe handler.

        :param request:
        :return:
        """
        form = SubscribeForm(request.POST)

        client = CodechaClient(settings.CODECHA_PRIVATE_KEY)
        result = client.verify(request.POST.get('codecha_challenge_field'),
                               request.POST.get('codecha_response_field'),
                               _get_ip(request))

        if not result:
            form.non_field_errors = ["Please solve Codecha",]
            return render(request,
                          LANDING_TEMPLATE,
                          {'codecha_key': settings.CODECHA_PUBLIC_KEY,
                           'form': form})

        if not form.is_valid():
            return render(request,
                          LANDING_TEMPLATE,
                          {'codecha_key': settings.CODECHA_PUBLIC_KEY,
                           'form': form})

        subscriber = form.subscribe(request)

        try:
            subscriber.full_clean()
        except ValidationError as exception:
            if exception.message_dict:
                for field, errors in exception.message_dict.iteritems():
                    err = form._errors.setdefault(field, ErrorList())
                    for error in errors:
                        err.append(error)
            else:
                form.non_field_errors = exception
            return render(request,
                          LANDING_TEMPLATE,
                          {'codecha_key': settings.CODECHA_PUBLIC_KEY,
                           'form': form})

        subscriber.save()

        response = "You are subscribed"
        return HttpResponse(response)


def _get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip
