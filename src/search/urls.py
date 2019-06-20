from django.conf.urls import include, url
from django.urls import path
import haystack

from . import views

app_name = 'search'

urlpatterns = [
    #url(r'^$', include('haystack.urls')),
    path('', views.search, name='searchpage')
]
