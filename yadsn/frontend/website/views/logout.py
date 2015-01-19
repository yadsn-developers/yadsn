from django.shortcuts import redirect
from django.views.generic import View

from yadsn.catalogs import models


class Logout(View):

    auth_model = models.Catalog.auth

    def get(self, request):
        self.auth_model().logout(request)
        return redirect('website:profile')
