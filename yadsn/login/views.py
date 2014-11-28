from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import View


LOGIN_TEMPLATE = 'login/login_form.html'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid login credentials")
        return self.cleaned_data

    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class Index(View):
    def get(self, request):
        return render(request,
                      LOGIN_TEMPLATE,
                      {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
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