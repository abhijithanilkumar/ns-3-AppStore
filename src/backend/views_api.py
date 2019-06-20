import json
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from apps.models import App, Release
from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse
from .serializers import App as AppObject, AppSerializer
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def install(request, module_name, version=None):
    app_found = True
    try:
        app = App.objects.get(name=module_name)
    except BaseException:
        # Request 404 for App not found on the AppStore
        app_found = False
        message = "Module: " + module_name + " was not found on the ns-3 AppStore."
    # if version is not specified in the API Call, send the latest file config, 
    # else the specified version config
    if version==None:
        app_release = Release.objects.filter(app=app).order_by('-version').first()
    else:
        app_release = Release.objects.filter(app=app, version=version).first()
        # Send 404 for App with not the requested version
        if app_release==None:
            app_found = False
            message = "Module: " + module_name + " with version: " + version + " was not found on the ns-3 AppStore."

    if app_release and str(app_release.filename):
        bakefile_url = settings.MEDIA_URL + str(app_release.filename)
    else:
        bakefile_url = None

    # Return the response based on whether the app is found or not
    if app_found:
        message = "Module: " + module_name + " with version: " + app_release.version + " found on the ns-3 AppStore."
        app_object = AppObject(name=app.name, app_type=app.app_type, coderepo=app.coderepo, version=app_release.version, ns=app_release.require.name, bakefile_url=bakefile_url, message=message)
        app_serialized = AppSerializer(app_object)
        return Response(data=app_serialized.data, status=200)
    else:
        app_object = AppObject(message=message)
        app_serialized = AppSerializer(app_object)
        return Response(data=app_serialized.data, status=404)        


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
