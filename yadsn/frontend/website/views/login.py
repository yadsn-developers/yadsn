from django.shortcuts import render
from django.views.generic import View
from djpybinder import inject, inject_provider


@inject('auth', from_namespace='users.models')
@inject_provider('login_form', from_namespace='users.forms')
class Login(View):

    TEMPLATE = 'login/index.html'

    def get(self, request):
        return render(request, self.TEMPLATE)

    def post(self, request):
        return render(request, self.TEMPLATE)
