from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from backend import users


class Login(View):

    TEMPLATE = 'login/index.html'
    catalog = users.Catalog(users.Catalog.auth_manager,
                            users.Catalog.login_form)

    def get(self, request):
        return render(request,
                      self.TEMPLATE,
                      {'form': self.catalog.login_form()})

    def post(self, request):
        form = self.catalog.login_form(request.POST)
        if not form.is_valid:
            return render(request, self.TEMPLATE, {'form': form})
        user = self.catalog.auth_manager().login(**form.cleaned_data)
        return HttpResponse("Hello " + user.username)
