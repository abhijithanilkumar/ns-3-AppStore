from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<num>[0-9]+)/$', views.appPage, name="appPage"),
    url(r'^download/(?P<num>[0-9]+)/$', views.download, name="download"),
    url(r'^tag/$', views.tagSearch, name="allApps"),
    url(r'^tag/(?P<num>[0-9]+)/$', views.tagSearch, name="tagSearch"),
    url(r'^author/(?P<num>[0-9]+)/$', views.authorSearch, name="authorSearch"),
]
