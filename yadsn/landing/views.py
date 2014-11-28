from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib import messages
from codecha import CodechaClient
from models import Subscriber


def index(request):
    """
    Landing index page.

    :param request:
    :return:
    """
    return render(request,
                  'landing/login_form.html',
                  {'codecha_key': settings.CODECHA_PUBLIC_KEY})


def subscribe(request):
    """
    Landing subscribe handler.

    :param request:
    :return:
    """
    client = CodechaClient(settings.CODECHA_PRIVATE_KEY)
    result = client.verify(request.POST.get('codecha_challenge_field'),
                           request.POST.get('codecha_response_field'),
                           _get_ip(request))

    if not result:
        messages.error(request, 'Please solve Codecha')
        return redirect(reverse('landing:index'), request)

    subscriber = Subscriber(email=request.POST.get('email'),
                            codecha_language=request.POST.get('codecha_language'),
                            http_referrer=request.META.get('HTTP_REFERER'))

    try:
        subscriber.full_clean()
    except ValidationError as exception:
        for field, errors in exception.message_dict.iteritems():
            for error in errors:
                messages.error(request, ': '.join([field, error]))
        return redirect(reverse('landing:index'), request)

    subscriber.save()

    messages.success(request, 'You are subscribed')
    return redirect(reverse('landing:index'), request)


def _get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip