from django.conf.urls import url

from .views import Graph


urlpatterns = [
    url(r'^graph/$', Graph.as_view(), name='graph'),
]
