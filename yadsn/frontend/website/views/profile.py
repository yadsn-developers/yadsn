from django.shortcuts import render
from django.views.generic import View
from django.conf import settings


class Profile(View):

    TEMPLATE = 'profile/index.html'

    def get(self, request):
        se_manager = settings.SE_MANAGER_CLS(**settings.STACKEXCHANGE_MANAGER_KEYS)
        se_user = se_manager.get_se_user(request.user)
        return render(request,
                      self.TEMPLATE,
                      {'user': request.user,
                       'se_user': se_user})