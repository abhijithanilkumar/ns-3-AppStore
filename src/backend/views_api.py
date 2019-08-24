import json
import datetime
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from apps.models import App, Release
from util.views import ipaddr_str_to_long
from download.models import Download, ReleaseDownloadsByDate
from django.conf import settings
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import App as AppObject, AppSerializer, AppSearchSerializer, AppReleaseSerializer


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


@api_view(['POST'])
@throttle_classes([AnonRateThrottle])
def install(request):
    module_name = request.data.get('module_name')
    version = request.data.get('version')
    ns = request.data.get('ns')
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

    if app_release.require.name in ns:
        app_object = AppObject(
            name=app.name,
            app_type=app.app_type,
            coderepo=app.coderepo,
            version=app_release.version,
            ns=app_release.require.name,
            bakefile_url=bakefile_url,
            message=message)
        app_serialized = AppSerializer(app_object)

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

    return Response(data=app_serialized.data, status=200)


class SearchApiViewSet(viewsets.ViewSet):

    @throttle_classes([AnonRateThrottle])
    def list(self, request):
        if request.GET:
            query = request.GET.get('q')
            page = request.GET.get('page')
            if query:
                queryset = App.objects.filter(Q(name__icontains=query)
                                              | Q(abstract__icontains=query))
                app_release = Release.objects.filter(
                    app__in=queryset).order_by('-version')
                if page is not None:
                    paginator = PageNumberPagination()
                    context = paginator.paginate_queryset(app_release, request)
                    serializer = AppReleaseSerializer(context, many=True)
                    return paginator.get_paginated_response(serializer.data)
                else:
                    serializer = AppReleaseSerializer(app_release, many=True)
                    if len(serializer.data):
                        return Response(serializer.data, 200)
                    else:
                        return Response(serializer.data, 404)
            elif query is None and page is not None:
                queryset = App.objects.all()
                paginator = PageNumberPagination()
                context = paginator.paginate_queryset(queryset, request)
                serializer = AppSearchSerializer(context, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                return Response([], 404)
        else:
            queryset = App.objects.all()
            serializer = AppSearchSerializer(queryset, many=True)
            return Response(serializer.data, 200)


    @throttle_classes([AnonRateThrottle])
    def create(self, request):
        """
        Handles search based on the ns version & query
        """
        ns = request.data.get('ns')
        query = request.data.get('q')
        if query and ns:
            queryset = App.objects.filter(Q(name__icontains=query)
                                                  | Q(abstract__icontains=query))
            app_release = Release.objects.filter(
                        app__in=queryset).order_by('-version')
            context = set()
            for app in app_release:
                if str(app.require) in ns:
                    context.add(app)
            serializer = AppReleaseSerializer(context, many=True)
            return Response(serializer.data, 200)
        elif query is None and ns is None:
            queryset = App.objects.all()
            serializer = AppSearchSerializer(queryset, many=True)
            return Response(serializer.data, 200)
        else:
            return Response([], 404)