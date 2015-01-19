from django.shortcuts import redirect
from django.views.generic import View
from backend.users.models.user import Users

# TODO: exception handling


class SeCallback(View):

    def get(self, request):
        user_manager = Users()
        user_manager.set_se_token(request.user, request.GET['code'])
        user_manager.fill_se_profile(request.user, ['reputation', 'link'])
        return redirect('website:profile')