import json
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.models import App, Release
from util.views import ipaddr_str_to_long
from download.models import Download, ReleaseDownloadsByDate
from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse

def _client_ipaddr(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ipaddr_str = forwarded_for.split(',')[0]
    else:
        ipaddr_str = request.META.get('REMOTE_ADDR')
    return ipaddr_str_to_long(ipaddr_str)


def _increment_count(klass, **args):
    obj, created = klass.objects.get_or_create(**args)
    obj.count += 1
    obj.save()


@api_view(['GET'])
def install(request, module_name, version=None):
    response = {}
    try:
        app = App.objects.get(name=module_name)
    except BaseException:
        # Request 404 for App not found on the AppStore
        response['status'] = 404
        response['message'] = "Module: " + module_name + " was not found on the ns-3 AppStore."
        return Response(response)
    # if version is not specified in the API Call, send the latest file config, 
    # else the specified version config
    if version==None:
        app_release = Release.objects.filter(app=app).order_by('-version').first()
    else:
        app_release = Release.objects.filter(app=app, version=version).first()
        # Send 404 for App with not the requested version
        if app_release==None:
            response['status'] = 404
            response['message'] = "Module: " + module_name + " with version: " + version + " was not found on the ns-3 AppStore."
            return Response(response)

    response['name'] = app.name
    response['app_type'] = app.app_type
    response['coderepo'] = app.coderepo
    response['version'] = app_release.version
    if str(app_release.filename):
        response['bakefile_url'] = settings.MEDIA_URL + str(app_release.filename)
    else:
        response['bakefile_url'] = None
    response['status'] = 200
    response['message'] = "Module: " + module_name + " with version: " + app_release.version + " found on the ns-3 AppStore."
    response = json.loads(json.dumps(response))

    ## Update the download statistics
    ip4addr = _client_ipaddr(request)
    when = datetime.date.today()
    
    # Update the App object
    app_release.app.downloads += 1
    app_release.app.save()

     # Record the download as a Download object
    Download.objects.create(release=app_release, ip4addr=ip4addr, when=when)
    
    # Record the download in the timeline
    _increment_count(ReleaseDownloadsByDate, release = app_release, when = when)
    _increment_count(ReleaseDownloadsByDate, release = None, when = when)

    return Response(response)


@api_view(['GET'])
def search(request):
    query = request.GET.get('q')
    apps = App.objects.filter(Q(name__icontains=query) | Q(abstract__icontains=query))
    response = []
    for app in apps:
        temp_app = {}
        try:
            app_release = Release.objects.filter(app=app).order_by('-version').first()
            temp_app['version'] = app_release.version
        except BaseException:
            temp_app['version'] = None
        temp_app['name'] = app.name
        temp_app['title'] = app.title
        temp_app['abstract'] = app.abstract
        response.append(temp_app)
        
    return Response(list(response))