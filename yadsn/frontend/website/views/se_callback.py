from django.shortcuts import redirect
from django.views.generic import View
from django.conf import settings
from backend.users.models.database import StackExchangeProfile

# TODO: profile render duplication [template extension]
# TODO: exception handling
# TODO: inject SE client


class SeCallback(View):

    def get(self, request):
        se_client = settings.SE_CLIENT_CLS(**settings.STACKEXCHANGE_CLIENT_KEYS)
        token = se_client.get_token(request.GET['code'])
        request.user.se_profile = StackExchangeProfile(**token)
        request.user.save()
        return redirect('website:profile')