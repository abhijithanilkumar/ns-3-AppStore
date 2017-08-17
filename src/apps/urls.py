from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<name>[\w\-]+)/$', views.appPage, name="appPage"),
    url(r'^download/(?P<num>[0-9]+)/$', views.download, name="download"),
    url(r'^tag/all/$', views.tagSearch, name="allApps"),
    url(r'^tag/(?P<name>[\w\-]+)/$', views.tagSearch, name="tagSearch"),
    url(r'^feedback/(?P<num>[0-9]+)/$', views.feedback, name="feedback"),
]
