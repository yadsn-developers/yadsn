from django.shortcuts import render
from django.views.generic import View
from yadsn.catalogs import inject, inject_provider


@inject('auth', from_namespace='users')
@inject_provider('login_form', from_namespace='users')
class Login(View):

    TEMPLATE = 'login/index.html'

    def get(self, request):
        return render(request, self.TEMPLATE)

    def post(self, request):
        return render(request, self.TEMPLATE)
