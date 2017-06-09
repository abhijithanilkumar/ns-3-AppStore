from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.appPage, name="apps"),
    url(r'^(?P<num>[0-9]+)/$', views.appPage, name="appPage"),
]
