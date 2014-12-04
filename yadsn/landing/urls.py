from django.conf.urls import url
from yadsn.catalogs import views

urlpatterns = [
    url(r'^$', views.provide('landing_index'), name='index'),
]
