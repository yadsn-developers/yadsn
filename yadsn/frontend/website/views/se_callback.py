from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from djpybinder import inject, inject_provider
from backend.stackexchange import SE_CLIENT_CLS
from django.conf import settings

# TODO: inject SE client

# TODO: exception handling
# TODO: profile render duplication [template extension]
# TODO: move settings out from git https://stackoverflow.com/questions/4909958/django-local-settings


class SeCallback(View):

    TEMPLATE = 'profile/index.html'

    def get(self, request):
        se_client = SE_CLIENT_CLS(**settings.STACKEXCHANGE_KEYS)
        token = se_client.get_token(request.GET['code'])
        se_user = se_client.get_se_user(token['access_token'])
        return render(request,
                      self.TEMPLATE,
                      {'user': request.user,
                       'se_user': se_user})