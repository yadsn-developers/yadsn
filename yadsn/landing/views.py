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

    result = client.verify(request.POST.get('codecha_challenge_field', None),
                           request.POST.get('codecha_response_field', None),
                           request.META['REMOTE_ADDR'])

    if not result:
        messages.error(request, 'Please solve Codecha')
        return redirect(reverse('landing:index'), request)

    subscriber = Subscriber(email=request.POST['email'],
                            codecha_language=request.POST['codecha_language'],
                            http_referrer=request.META['HTTP_REFERER'])

    try:
        subscriber.full_clean()
        subscriber.save()

    except ValidationError as error:
        for error_message in error.message_dict:
            messages.error(request, ': '.join([error_message, error.message_dict[error_message][0]]))
        return redirect(reverse('landing:index'), request)

    messages.success(request, 'You are subscribed')
    return redirect(reverse('landing:index'), request)
