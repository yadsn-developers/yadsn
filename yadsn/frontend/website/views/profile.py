from django.shortcuts import render
from django.views.generic import View
from django.conf import settings


class Profile(View):

    TEMPLATE = 'profile/index.html'

    def get(self, request):
        return render(request,
                      self.TEMPLATE,
                      {'user': request.user})