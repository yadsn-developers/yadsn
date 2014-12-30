from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from djpybinder import inject, inject_provider
from backend.stackexchange.client import StackexchangeClient
from django.conf import settings

# TODO: mock the SE user response
# TODO: exception handling
# TODO: se_client instance duplication
# TODO: profile render duplication
# TODO: inject SE client
# TODO: move settings out from git


class SeCallback(View):

    TEMPLATE = 'profile/index.html'

    def get(self, request):
        se_client = StackexchangeClient(**settings.STACKEXCHANGE_KEYS)
        token = se_client.get_token(request.GET['code'])
        se_user = se_client.get_se_user(token['access_token'])
        return render(request,
                      self.TEMPLATE,
                      {'user': request.user,
                       'se_user': se_user})