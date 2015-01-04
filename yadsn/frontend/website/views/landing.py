from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.views.generic import View
from django.http import HttpResponse
from django.forms.util import ErrorList

from backend import users


class Landing(View):

    catalog = users.Catalog(users.Catalog.subscriptions_form,
                            users.Catalog.subscriptions_manager)

    TEMPLATE = 'landing/index.html'

    def get(self, request):
        self.catalog.subscriptions_manager()

        return render(request,
                      self.TEMPLATE,
                      {'form': self.catalog.subscriptions_form()})

    def post(self, request):
        additional_data = {'client_ip': _get_ip(request),
                           'http_referrer': request.META['HTTP_REFERER']}

        form = self.catalog.subscriptions_form(
            dict(request.POST.items() + additional_data.items())
        )

        if not form.is_valid():
            return render(request, self.TEMPLATE, {'form': form})

        try:
            self.catalog.subscriptions_manager().subscribe(**form.cleaned_data)
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
