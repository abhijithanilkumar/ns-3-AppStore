# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import App, Release
from markdownx.utils import markdownify

# Create your views here.

def appPage(request, num=0):
    if num:
        app = get_object_or_404(App, id=num)
        app.description = markdownify(app.description)
        releases = Release.objects.filter(app=app).order_by('-id')
        for release in releases:
            release.notes = markdownify(release.notes)
        authors = app.authors.all()
        if releases:
            latest = releases.latest('id')
        else:
            latest = []
        return render(request, 'page.html', {'app':app, 'releases':releases, 'authors':authors, 'latest':latest})
    else:
        apps = App.objects.all()
        return render(request, 'page.html', {'apps':apps})
