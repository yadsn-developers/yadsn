from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from backend import users


class Login(View):

    login_form = users.Catalog.login_form
    auth_model = users.Catalog.auth_model

    TEMPLATE = 'login/index.html'

    def get(self, request):
        return render(request,
                      self.TEMPLATE,
                      {'form': self.login_form()})

    def post(self, request):
        form = self.login_form(request.POST)
        if not form.is_valid():
            return render(request, self.TEMPLATE, {'form': form})
        user = self.auth_model().login(**form.cleaned_data)
        return HttpResponse("Hello " + user.username)
