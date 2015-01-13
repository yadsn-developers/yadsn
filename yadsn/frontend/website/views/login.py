from django.shortcuts import render, redirect
from django.views.generic import View
from djpybinder import inject, inject_provider


@inject('auth', from_namespace='users.models')
@inject_provider('login_form', from_namespace='users.forms')
class Login(View):

    TEMPLATE = 'login/index.html'

    def get(self, request):
        return render(request,
                      self.TEMPLATE,
                      {'form': self.login_form()})

    def post(self, request):
        form = self.login_form(request.POST)
        if not form.is_valid():
            return render(request, self.TEMPLATE, {'form': form})
        user = self.auth.authenticate(**form.cleaned_data)
        self.auth.login(request,user)
        return redirect('website:profile')