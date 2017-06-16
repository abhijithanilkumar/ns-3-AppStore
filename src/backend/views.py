# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def createApp(request):
    return render(request, 'create.html')

@login_required
def editApp(request, num):
    return render(request, 'edit.html')

@login_required
def createRelease(request, num):
    return render(request, 'create_release.html')

@login_required
def editRelease(request, num):
    return render(request, 'edit_release.html')
