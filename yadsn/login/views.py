from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponse
from django.views.generic import View
from yadsn.catalogs import forms


LOGIN_TEMPLATE = 'login/login_form.html'


@forms.inject('login_form')
class Index(View):

    _login_form = None

    def get(self, request):
        return render(request,
                      LOGIN_TEMPLATE,
                      {'form': self._login_form()})

    def post(self, request):
        form = self._login_form(request.POST)
        if not form.is_valid():
            return render(request,
                          LOGIN_TEMPLATE,
                          {'form': form})
        user = form.login()
        if not user:
            return render(request,
                          LOGIN_TEMPLATE,
                          {'form': form})
        login(request, user)
        response = "Hello " + user.username
        return HttpResponse(response)
