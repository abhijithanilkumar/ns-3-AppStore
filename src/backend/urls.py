from django.conf.urls import url
from django.urls import path

from . import views
from . import views_api

app_name = 'backend'

urlpatterns = [
    path(
        'create/',
        views.createApp,
        name='create'),
    path(
        'edit/<int:num>/',
        views.editApp,
        name='edit'),
    path(
        'create/release/<int:num>/',
        views.createRelease,
        name='createRelease'),
    path(
        'edit/release/<int:num>/',
        views.editRelease,
        name='editRelease'),
    path(
        'maintenance/<int:num>/',
        views.modifyMaintenance,
        name='modify_maintenance'),
    path(
        'installation/<int:num>/',
        views.modifyInstallation,
        name='modify_installation'),
    path(
        'download/<int:num>/',
        views.modifyDownload,
        name='modify_download'),
    path(
        'development/<int:num>/',
        views.modifyDevelopment,
        name='modify_development'),
    path(
        'details/<int:num>/',
        views.editDetails,
        name='edit_details'),
    path(
        'releasedelete/<int:num>/',
        views.deleteReleasePrompt,
        name='delete_release_prompt'),
    path(
        'releasedelconf/<int:num>/',
        views.deleteRelease,
        name='delete_release'),
    path(
        'screenshots/<int:num>/',
        views.screenshots,
        name='screenshots'),
    path(
        'screenshotdelete/<int:num>/',
        views.deleteScreenshotPrompt,
        name='delete_screenshot_prompt'),
    path(
        'screenshotdelconf/<int:num>/',
        views.deleteScreenshot,
        name='delete_screenshot'),
    path(
        'api/install/<str:module_name>/',
        views_api.install,
        name='install'),
    path(
        'api/install/<str:module_name>/<str:version>/',
        views_api.install,
        name='install'),
    path(
        'api/search/',
        views_api.SearchApiViewSet.as_view({'post': 'create'}),
        name='search'),
    path(
        'api/search/',
        views_api.SearchApiViewSet.as_view({'get': 'list'}),
        name='search'),
]
