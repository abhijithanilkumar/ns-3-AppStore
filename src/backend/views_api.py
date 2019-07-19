import json
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from apps.models import App, Release
from django.conf import settings
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import App as AppObject, AppSerializer, AppSearchSerializer, AppReleaseSerializer


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
        elif query:
            queryset = App.objects.all()
            serializer = AppSearchSerializer(queryset, many=True)
            return Response(serializer.data, 200)
        else:
            return Response([], 404)