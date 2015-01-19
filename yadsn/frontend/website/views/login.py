from django.shortcuts import render, redirect
from django.views.generic import View

from backend.users.models.auth import Auth
from backend.users.forms import LoginForm


class Login(View):

    TEMPLATE = 'login/index.html'

    def get(self, request):
        return render(request,
                      self.TEMPLATE,
                      {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, self.TEMPLATE, {'form': form})
        auth = Auth()
        user = auth.authenticate(**form.cleaned_data)
        auth.login(request,user)
        return redirect('website:profile')