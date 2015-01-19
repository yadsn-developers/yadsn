from django.shortcuts import redirect
from django.views.generic import View

from yadsn.catalogs import models
# TODO: exception handling


class SeCallback(View):

    users = models.Catalog.users

    def get(self, request):
        user_manager = self.users()
        user_manager.set_se_token(request.user, request.GET['code'])
        user_manager.fill_se_profile(request.user, ['reputation', 'link'])
        return redirect('website:profile')
