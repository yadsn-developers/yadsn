from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.views.generic import View
from django.http import HttpResponse
from django.forms.util import ErrorList


LANDING_TEMPLATE = 'landing/index.html'


class Index(View):

    _codecha_client = None
    _subscribe_form = None

    def get(self, request):
        """
        Landing index page.

        :param request:
        :return:
        """
        return render(request,
                      LANDING_TEMPLATE,
                      {'codecha_key': self._codecha_client().public_key,
                       'form': self._subscribe_form()})

    def post(self, request):
        """
        Landing subscribe handler.

        :param request:
        :return:
        """
        form = self._subscribe_form(request.POST)
        codecha_client = self._codecha_client()

        result = codecha_client.verify(
            request.POST.get('codecha_challenge_field'),
            request.POST.get('codecha_response_field'),
            _get_ip(request))

        if not result:
            form.non_field_errors = ["Please solve Codecha",]
            return render(request,
                          LANDING_TEMPLATE,
                          {'codecha_key': codecha_client.public_key,
                           'form': form})

        if not form.is_valid():
            return render(request,
                          LANDING_TEMPLATE,
                          {'codecha_key': codecha_client.public_key,
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
                          {'codecha_key': codecha_client.public_key,
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
