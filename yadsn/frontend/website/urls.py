from django.conf.urls import url

from .views.landing import Landing
from .views.login import Login


urlpatterns = [
    url(r'^$', Landing.as_view(), name='landing'),
    url(r'^login/$', Login.as_view(), name='login'),
]
