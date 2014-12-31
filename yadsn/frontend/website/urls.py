from django.conf.urls import url

from .views.landing import Landing
from .views.happy_new_year import HappyNewYear
from .views.login import Login


urlpatterns = [
    url(r'^$', Landing.as_view(), name='landing'),
    url(r'^happy_new_year/$', HappyNewYear.as_view(), name='happy_new_year'),
    url(r'^login/$', Login.as_view(), name='login'),
]
