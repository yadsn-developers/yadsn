from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from djpybinder import inject
from backend.stackexchange.client import StackexchangeClient
from django.conf import settings


class SeCallback(View):

    TEMPLATE = 'profile/index.html'

    def get(self, request):
        se_client = StackexchangeClient(
                           client_id=settings.SE_CLIENT_ID,
                           scope='',
                           client_secret=settings.SE_CLIENT_SECRET,
                           key=settings.SE_KEY,
                           redirect_uri=settings.SE_REDIRECT_URI)
        access_token = se_client.get_token(request.GET['code'])
        se_user = se_client.get_se_user(access_token)
        return render(request,
                      self.TEMPLATE,
                      {'user': request.user,
                       'se_user': se_user})