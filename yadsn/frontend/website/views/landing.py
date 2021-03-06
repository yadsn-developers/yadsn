from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.views.generic import View
from django.http import HttpResponse
from django.forms.util import ErrorList

from backend.users.models.user import Subscriptions
from backend.users.forms import SubscriptionForm
from backend.codecha.client import CodechaClient
from django.conf import settings


class Landing(View):

    TEMPLATE = 'landing/index.html'

    def get(self, request):
        return render(request,
                      self.TEMPLATE,
                      {'form': SubscriptionForm(codecha_client=CodechaClient(**settings.CODECHA_KEYS))})

    def post(self, request):
        additional_data = {'client_ip': _get_ip(request),
                           'http_referrer': request.META['HTTP_REFERER']}
        form = SubscriptionForm(dict(request.POST.items() +
                                     additional_data.items()), codecha_client=CodechaClient(**settings.CODECHA_KEYS))
        if not form.is_valid():
            return render(request, self.TEMPLATE, {'form': form})

        try:
            Subscriptions().subscribe(**form.cleaned_data)
        except ValidationError as exception:
            if exception.message_dict:
                for field, errors in exception.message_dict.iteritems():
                    err = form._errors.setdefault(field, ErrorList())
                    for error in errors:
                        err.append(error)
            else:
                form.non_field_errors = exception
            return render(request, self.TEMPLATE, {'form': form})

        return HttpResponse('You are subscribed')


def _get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip
