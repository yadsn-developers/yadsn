from django.shortcuts import render
from django.views.generic import View
from yadsn.catalogs import forms, models


@models.inject('auth')
@forms.inject_provider('login_form')
class Login(View):

    TEMPLATE = 'login/index.html'

    def get(self, request):
        """
        Landing index page.

        :param request:
        :return:
        """
        return render(request, self.TEMPLATE)

    def post(self, request):
        """
        Landing subscribe handler.

        :param request:
        :return:
        """
        return render(request,
                      self.TEMPLATE)
