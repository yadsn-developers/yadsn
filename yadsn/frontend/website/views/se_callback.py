from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse
from djpybinder import inject
from backend.stackexchange.client import StackexchangeClient
from django.conf import settings


class SeCallback(View):

    def get(self, request):
        return HttpResponse(request.GET['code'])