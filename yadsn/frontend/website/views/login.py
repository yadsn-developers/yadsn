from django.shortcuts import render, redirect
from django.views.generic import View

from yadsn.catalogs import forms
from yadsn.catalogs import models


class Login(View):

    login_form = forms.Catalog.login
    auth_model = models.Catalog.auth

    TEMPLATE = 'login/index.html'

    def get(self, request):
        return render(request,
                      self.TEMPLATE,
                      {'form': self.login_form()})

    def post(self, request):
        form = self.login_form(request.POST)
        if not form.is_valid():
            return render(request, self.TEMPLATE, {'form': form})
        auth = self.auth_model()
        user = auth.authenticate(**form.cleaned_data)
        auth.login(request, user)
        return redirect('website:profile')
