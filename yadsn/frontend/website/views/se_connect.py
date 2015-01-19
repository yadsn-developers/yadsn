from django.shortcuts import redirect
from django.views.generic import View

from yadsn.catalogs import services


class SeConnect(View):

    stack_exchange = services.Catalog.stack_exchange

    def get(self, _):
        return redirect(self.stack_exchange().connect().url)
