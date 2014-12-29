from django.shortcuts import redirect
from django.views.generic import View
from djpybinder import inject
from backend.stackexchange.client import StackexchangeClient
from django.conf import settings


class SeConnect(View):

    def get(self, request):
        se_client = StackexchangeClient(
                           client_id=settings.SE_CLIENT_ID,
                           scope='',
                           client_secret=settings.SE_CLIENT_SECRET,
                           key=settings.SE_KEY,
                           redirect_uri=settings.SE_REDIRECT_URI)
        return redirect(se_client.connect().url)