from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic import View


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())


class Index(View):
    def get(self, request):
        return render(request,
                      'login/login_form.html',
                      {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return redirect(reverse('login:index'), request)
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if not user:
            return redirect(reverse('login:index'), request)
        response = "Hello " + user.username
        return HttpResponse(response)