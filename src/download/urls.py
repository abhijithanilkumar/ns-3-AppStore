from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'download'

urlpatterns = [
    path(
        'stats/',
        views.all_stats,
        name='all_stats'),
    path(
        'stats/timeline',
        views.all_stats_timeline,
        name='all_stats_timeline'),
    path(
        'stats/<slug:name>',
        views.app_stats,
        name='app_stats'),
    path(
        'stats/<slug:name>/timeline',
        views.app_stats_timeline,
        name='app_stats_timeline')
]
