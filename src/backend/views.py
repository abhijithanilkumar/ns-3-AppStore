# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import CreateAppForm, EditAppForm, ReleaseForm
from django.apps import apps

@login_required
def createApp(request):
    if request.user.is_staff:
        if request.method == 'GET':
            form = CreateAppForm()
        elif request.method == 'POST':
            form = CreateAppForm(request.POST)
            if form.is_valid():
                new_app = form.save()
                new_app.save()
                return render(request, 'message.html', {'message': "New App Page created Successfully!"})
    else:
        return render(request, 'message.html', {'message': "You are not authorized to view this page!"})
    return render(request, 'create.html', {'form':form})

@login_required
def editApp(request, num):
    App = apps.get_model('apps', 'App')
    try:
        edit_app = App.objects.get(id=num)
    except:
        return render(request, 'message.html', {'message': "Requested App does not Exist!"})
    editors = edit_app.editors.all()
    if request.user in editors or request.user.is_staff:
        if request.method == 'GET':
            form = EditAppForm(instance=edit_app)
        elif request.method == 'POST':
            form = EditAppForm(request.POST, instance=edit_app)
            if form.is_valid():
                edited_app = form.save()
                edited_app.save()
                return render(request, 'message.html', {'message': "App Page edited Successfully!"})
    else:
        return render(request, 'message.html', {'message': "You are not authorized to view this page!"})
    return render(request, 'edit.html', {'form':form})

@login_required
def createRelease(request, num):
    App = apps.get_model('apps', 'App')
    try:
        release_app = App.objects.get(id=num)
    except:
        return render(request, 'message.html', {'message': "Requested App does not Exist!"})
    editors = release_app.editors.all()
    if request.user in editors or request.user.is_staff:
        if request.method == 'GET':
            form = ReleaseForm()
        elif request.method == 'POST':
            form = ReleaseForm(request.POST)
            if form.is_valid():
                new_release = form.save(commit=False)
                new_release.app = release_app
                new_release.save()
                return render(request, 'message.html', {'message': "Release added Successfully!"})
    else:
        return render(request, 'message.html', {'message': "You are not authorized to view this page!"})
    return render(request, 'create_release.html', {'form':form})

@login_required
def editRelease(request, num):
    Release = apps.get_model('apps', 'Release')
    App = apps.get_model('apps', 'App')
    try:
        edit_release = Release.objects.get(id=num)
    except:
        return render(request, 'message.html', {'message': "Requested App does not Exist!"})
    editors = edit_release.app.editors.all()
    if request.user in editors or request.user.is_staff:
        if request.method == 'GET':
            form = ReleaseForm(instance=edit_release)
        elif request.method == 'POST':
            form = ReleaseForm(request.POST, instance=edit_release)
            if form.is_valid():
                edited_release = form.save()
                edited_release.save()
                return render(request, 'message.html', {'message': "Release edited Successfully!"})
    else:
        return render(request, 'message.html', {'message': "You are not authorized to view this page!"})
    return render(request, 'edit_release.html', {'form':form})
