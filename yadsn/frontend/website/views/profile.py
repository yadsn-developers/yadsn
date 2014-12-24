from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required


class Profile(View):

    TEMPLATE = 'profile/index.html'

    def get(self, request):
        return render(request,
                      self.TEMPLATE,
                      {'user': request.user})