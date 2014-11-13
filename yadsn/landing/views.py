from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from helpers.codecha import Codecha
from models import Subscriber

CODECHA_PUBLIC_KEY = "c717b24a797041b79d27e54ed6cee53b"
CODECHA_PRIVATE_KEY = "3856e53084634b6b8e82f9bf26cb6c30"


def index(request):
    return render(
        request,
        'index.html',
        {
            'codecha_key': CODECHA_PUBLIC_KEY,
        },
    )


def subscribe(request):
    codecha_challenge = request.POST['codecha_challenge_field']
    codecha_response = request.POST['codecha_response_field']
    codecha_key = CODECHA_PRIVATE_KEY
    ip = request.META['REMOTE_ADDR']

    if codecha_challenge and codecha_response:
        codecha_success = Codecha.verify(codecha_challenge, codecha_response, ip, codecha_key)
    else:
        codecha_success = False

    if not codecha_success:
        return HttpResponseRedirect(
            reverse('landing:index'),
            {
                'codecha_key': CODECHA_PUBLIC_KEY,
                'error_message': 'Please solve the Codecha',
            }
        )
    else:
        subscriber = Subscriber(
            email=request.POST['email'],
            codecha_language='Python',
            http_referrer='None'
        )
        subscriber.save()
        return HttpResponseRedirect(
            reverse('landing:index'),
            {
                'codecha_key': CODECHA_PUBLIC_KEY,
                'error_message': 'You are subscribed',
            }
        )

