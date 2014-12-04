from django.conf.urls import url
from yadsn.catalogs import views

urlpatterns = [
    url(r'^$', views.provide('login_index'), name='index'),
]
