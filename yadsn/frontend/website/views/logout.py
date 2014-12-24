from django.shortcuts import redirect
from django.views.generic import View
from djpybinder import inject


@inject('auth', from_namespace='users.models')
class Logout(View):

    def get(self, request):
        self.auth.logout(request)
        return redirect('website:profile')
