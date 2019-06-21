import json
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework import viewsets
from apps.models import App, Release
from django.conf import settings
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import App as AppObject, AppSerializer, AppSearch, AppSearchSerializer


@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def install(request, module_name, version=None):
    app = get_object_or_404(App, name=module_name)
    # if version is not specified in the API Call, send the latest file config,
    # else the specified version config
    if version is None:
        app_release = Release.objects.filter(
            app=app).order_by('-version').first()
    else:
        app_release = get_object_or_404(Release, app=app, version=version)

    # it reaches here implies the module is found
    bakefile_url = settings.MEDIA_URL + str(app_release.filename)
    message = "Module: " + module_name + " with version: " + \
        app_release.version + " found on the ns-3 AppStore."

    app_object = AppObject(
        name=app.name,
        app_type=app.app_type,
        coderepo=app.coderepo,
        version=app_release.version,
        ns=app_release.require.name,
        bakefile_url=bakefile_url,
        message=message)
    app_serialized = AppSerializer(app_object)

    return Response(data=app_serialized.data, status=200)


@api_view(['GET'])
def search(request):
    query = request.GET.get('q')
    apps = App.objects.filter(Q(name__icontains=query)
                              | Q(abstract__icontains=query))
    response = []
    for app in apps:
        temp_app = {}
        try:
            app_release = Release.objects.filter(
                app=app).order_by('-version').first()
            temp_app['version'] = app_release.version
        except BaseException:
            temp_app['version'] = None
        temp_app['name'] = app.name
        temp_app['title'] = app.title
        temp_app['abstract'] = app.abstract
        response.append(temp_app)

    return Response(list(response))


class SearchApiViewSet(viewsets.ViewSet):
    def list(self, request):
        query = request.GET.get('q')
        queryset = App.objects.filter(Q(name__icontains=query)
                              | Q(abstract__icontains=query))
        serializer = AppSearchSerializer(queryset, many=True)
        return Response(serializer.data)

