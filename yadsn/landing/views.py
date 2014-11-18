from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import IntegrityError
from django.contrib import messages
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
        messages.error(request, 'Please solve Codecha')
        return redirect(reverse('landing:index'), request)

    # TODO: fetch the selected language from codecha

    try:
        validate_email(request.POST['email'])
        Subscriber.objects.create(email=request.POST['email'],
                                  codecha_language='Python', # request.POST.get('codecha_language')
                                  http_referrer=request.META['HTTP_REFERER'])
    except ValidationError, error:
        messages.error(request, error.message)
        return redirect(reverse('landing:index'), request)

    except IntegrityError:
        messages.error(request, 'This email is already subscribed')
        return redirect(reverse('landing:index'), request)

    messages.success(request, 'You are subscribed')
    return redirect(reverse('landing:index'), request)
