from django.shortcuts import redirect
from django.views.generic import View
from djpybinder import inject
from backend.stackexchange import SE_CLIENT_CLS
from django.conf import settings


class SeConnect(View):

    def get(self, request):
        se_client = SE_CLIENT_CLS(**settings.STACKEXCHANGE_KEYS)
        return redirect(se_client.connect().url)