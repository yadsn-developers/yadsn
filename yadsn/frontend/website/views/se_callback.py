from django.shortcuts import redirect
from django.views.generic import View
from backend.users.models.user import Users

# TODO: exception handling
# TODO: inject SE client


class SeCallback(View):

    def get(self, request):
        user_manager = Users(request.user)
        user_manager.set_se_token(request.GET['code'])
        user_manager.fill_se_profile()
        return redirect('website:profile')