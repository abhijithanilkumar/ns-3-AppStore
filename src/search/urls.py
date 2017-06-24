from django.conf.urls import include, url
import haystack

from . import views

urlpatterns = [
    #url(r'^$', include('haystack.urls')),
    url(r'^$', views.search, name="searchpage")
]
