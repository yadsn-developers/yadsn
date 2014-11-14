from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import HttpResponseRedirect as Redirect
from helpers.codecha import CodechaClient
from models import Subscriber


def index(request):
    """
    Landing index page.

    :param request:
    :return:
    """
    return render(request,
                  'index.html',
                  {'codecha_key': settings.CODECHA_PUBLIC_KEY})


def subscribe(request):
    """
    Landing subscribe handler.

    :param request:
    :return:
    """
    client = CodechaClient(settings.CODECHA_PRIVATE_KEY)
    try:
        result = client.verify(request.POST['codecha_challenge_field'],
                               request.POST['codecha_response_field'],
                               request.META['REMOTE_ADDR'])
    except KeyError:
        result = False

    if not result:
        return Redirect(reverse('landing:index'),
                        {'codecha_key': settings.CODECHA_PUBLIC_KEY,
                         'message': 'Please solve the Codecha'})
    try:
        Subscriber.objects.create(email=request.POST['email'],
                                  codecha_language='Python',
                                  http_referrer='None')
    except KeyError:
        return Redirect(reverse('landing:index'),
                        {'codecha_key': settings.CODECHA_PUBLIC_KEY,
                         'message': 'Emain could not be blank'})

    return Redirect(reverse('landing:index'),
                    {'codecha_key': settings.CODECHA_PUBLIC_KEY,
                     'message': 'You are subscribed'})
