from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.createApp, name="create"),
    url(r'^edit/(?P<num>[0-9]+)/$', views.editApp, name="edit"),
    url(r'^create/release/(?P<num>[0-9]+)/$', views.createRelease, name="createRelease"),
    url(r'^edit/release/(?P<num>[0-9]+)/$', views.editRelease, name="editRelease"),
    url(r'^maintenance/(?P<num>[0-9]+)/$', views.modifyMaintenance, name='modify_maintenance'),
    url(r'^installation/(?P<num>[0-9]+)/$', views.modifyInstallation, name='modify_installation'),
    url(r'^download/(?P<num>[0-9]+)/$', views.modifyDownload, name='modify_download'),
    url(r'^development/(?P<num>[0-9]+)/$', views.modifyDevelopment, name='modify_development'),
    url(r'^details/(?P<num>[0-9]+)/$', views.editDetails, name='edit_details'),
    url(r'^releasedelete/(?P<num>[0-9]+)/$', views.deleteReleasePrompt, name='delete_release_prompt'),
    url(r'^releasedelconf/(?P<num>[0-9]+)/$', views.deleteRelease, name='delete_release'),
    url(r'^screenshots/(?P<num>[0-9]+)/$', views.screenshots, name='screenshots'),
    url(r'^screenshotdelete/(?P<num>[0-9]+)/$', views.deleteScreenshotPrompt, name='delete_screenshot_prompt'),
    url(r'^screenshotdelconf/(?P<num>[0-9]+)/$', views.deleteScreenshot, name='delete_screenshot'),
]
