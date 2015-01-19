from django.conf.urls import url

from .views.landing import Landing
from .views.login import Login
from .views.profile import Profile
from .views.logout import Logout
from .views.se_connect import SeConnect
from .views.se_callback import SeCallback
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', Landing.as_view(), name='landing'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^profile/$', login_required(Profile.as_view()), name='profile'),
    url(r'^se-connect/$', login_required(SeConnect.as_view()), name='se_connect'),
    url(r'^se-callback/$', login_required(SeCallback.as_view()), name='se_callback'),
]
