from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.views.generic import View
from django.http import HttpResponse
from django.forms.util import ErrorList
from yadsn.catalogs import forms, models


@models.inject('subscription_manager')
@forms.inject_provider('subscription_form')
class Landing(View):

    TEMPLATE = 'landing/index.html'

    def get(self, request):
        """
        Landing index page.

        :param request:
        :return:
        """
        return render(request,
                      self.TEMPLATE,
                      {'form': self.subscription_form()})

    def post(self, request):
        """
        Landing subscribe handler.

        :param request:
        :return:
        """
        additional_data = {'client_ip': _get_ip(request),
                           'http_referrer': request.META['HTTP_REFERER']}
        form = self.subscription_form(dict(request.POST.items() +
                                           additional_data.items()))
        if not form.is_valid():
            return render(request, self.TEMPLATE, {'form': form})

        try:
            self.subscription_manager.subscribe(**form.cleaned_data)
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
