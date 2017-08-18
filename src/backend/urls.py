from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.createApp, name="create"),
    url(r'^edit/(?P<num>[0-9]+)/$', views.editApp, name="edit"),
    url(r'^create/release/(?P<num>[0-9]+)/$', views.createRelease, name="createRelease"),
    url(r'^edit/release/(?P<num>[0-9]+)/$', views.editRelease, name="editRelease"),
    url(r'^maintenance/(?P<num>[0-9])/$', views.modifyMaintenance, name='modify_maintenance'),
    url(r'^installation/(?P<num>[0-9])/$', views.modifyInstallation, name='modify_installation'),
    url(r'^download/(?P<num>[0-9])/$', views.modifyDownload, name='modify_download'),
    url(r'^details/(?P<num>[0-9])/$', views.editDetails, name='edit_details'),
]
