from django.conf.urls import url
from .views import Landing


urlpatterns = [
    url(r'^$', Landing.as_view(), name='landing'),
]
