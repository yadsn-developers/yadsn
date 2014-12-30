from django.shortcuts import redirect
from django.views.generic import View
from djpybinder import inject
from backend.stackexchange.client import StackexchangeClient
from django.conf import settings


class SeConnect(View):

    def get(self, request):
        se_client = StackexchangeClient(**settings.STACKEXCHANGE_KEYS)
        return redirect(se_client.connect().url)