from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yadsn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^login/', include('login.urls', namespace='login')),
    url(r'^$', include('front.website.urls', namespace='front.website')),
    url(r'^admin/', include(admin.site.urls)),
)
