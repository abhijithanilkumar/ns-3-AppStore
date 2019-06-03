import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.models import App, Release
from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse


@api_view(['GET'])
def install(request, module_name, version=None):
	response = {}
	return Response(response)