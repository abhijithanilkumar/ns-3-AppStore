from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.createApp, name="create"),
    url(r'^edit/(?P<num>[0-9]+)/$', views.editApp, name="edit"),
    url(r'^create/release/(?P<num>[0-9]+)/$', views.createRelease, name="createRelease"),
    url(r'^edit/release/(?P<num>[0-9]+)/$', views.editRelease, name="editRelease"),
    url(r'^maintenance/(?P<num>[0-9])/$', views.modifyMaintenance, name='modify_maintenance'),
    url(r'^instructions/(?P<num>[0-9])/$', views.modifyInstructions, name='modify_instructions'),
    url(r'^details/(?P<num>[0-9])/$', views.editDetails, name='edit_details'),
]
