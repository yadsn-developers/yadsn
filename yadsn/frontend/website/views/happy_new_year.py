from django.shortcuts import render
from django.views.generic import View


class HappyNewYear(View):

    TEMPLATE = 'happy_new_year/index.html'

    def get(self, request):
        return render(request, self.TEMPLATE)
