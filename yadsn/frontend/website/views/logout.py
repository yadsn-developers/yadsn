from django.shortcuts import redirect
from django.views.generic import View
from backend.users.models.auth import Auth


class Logout(View):

    def get(self, request):
        Auth().logout(request)
        return redirect('website:profile')
