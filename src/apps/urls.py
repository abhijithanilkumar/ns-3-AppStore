from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.appPage, name="apps"),
    url(r'^(?P<num>[0-9]+)/$', views.appPage, name="appPage"),
    url(r'^top/$', views.topPage, name="topPage"),
    url(r'^new/$', views.newPage, name="newPage"),
]
