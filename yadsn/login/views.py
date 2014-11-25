from django.shortcuts import render
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())


def index(request):
    return render(request,
                  'login/login_form.html',
                  {'form': LoginForm()})

def login(request):
    pass
