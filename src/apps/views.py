# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import App

# Create your views here.

def appPage(request, num=0):
    if num:
        print "hello"
        app = get_object_or_404(App, id=num)
        return render(request, 'page.html', {'app':app})
    else:
        apps = App.objects.all()
        return render(request, 'page.html', {'apps':apps})
