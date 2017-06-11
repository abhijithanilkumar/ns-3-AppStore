# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import App, Release

# Create your views here.

def appPage(request, num=0):
    if num:
        app = get_object_or_404(App, id=num)
        releases = Release.objects.filter(app=app).order_by('-id')
        latest = releases.latest('id')
        return render(request, 'page.html', {'app':app, 'releases':releases, 'latest':latest})
    else:
        apps = App.objects.all()
        return render(request, 'page.html', {'apps':apps})
