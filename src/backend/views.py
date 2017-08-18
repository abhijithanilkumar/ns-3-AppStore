# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import CreateAppForm, EditAppForm, ReleaseForm, \
        InstallationForm, MaintenanceForm, EditDetailsForm, \
        DownloadForm
from django.apps import apps
from util.img_util import scale_img

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
            form = EditAppForm(request.POST, request.FILES, instance=edit_app)
            if form.is_valid():
                edited_app = form.save(commit=False)
                if 'icon' in request.FILES:
                    icon_file = request.FILES['icon']
                    edited_app.icon = scale_img(icon_file, icon_file.name, 128, 'both')
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

@login_required
def modifyInstallation(request, num):
    existing = False
    App = apps.get_model('apps', 'App')
    Installation = apps.get_model('apps', 'Installation')
    try:
        app = App.objects.get(id=num)
    except:
        return render(request, 'message.html', {'message': "Requested App does not Exits!"})
    if Installation.objects.filter(app=app).exists():
        existing = True
        edit_Installation = Installation.objects.get(app=app)
    if request.user.is_staff or request.user in app.editors.all():
        if request.method == 'GET':
            if existing:
                form = InstallationForm(instance=edit_installation)
            else:
                form = InstallationForm()
        elif request.method == 'POST':
            if existing:
                form = InstallationForm(request.POST, instance=edit_installation)
            else:
                form = InstallationForm(request.POST)
            if form.is_valid():
                if existing:
                    edited_installation = form.save()
                    edited_installation.save()
                else:
                    installation = form.save(commit=False)
                    installation.app = app
                    installation.save()
                return render(request, 'message.html', {'message': "Installation modified Successfully!"})
    else:
        return render(request, 'message.html', {'message': "You are not authorized to view this page!"})
    return render(request, 'installation.html', {'form':form})

@login_required
def modifyMaintenance(request, num):
    existing = False
    App = apps.get_model('apps', 'App')
    Maintenance = apps.get_model('apps', 'Maintenance')
    try:
        app = App.objects.get(id=num)
    except:
        return render(request, 'message.html', {'message': "Requested App does not Exits!"})
    if Maintenance.objects.filter(app=app).exists():
        existing = True
        edit_maintenance = Maintenance.objects.get(app=app)
    if request.user.is_staff or request.user in app.editors.all():
        if request.method == 'GET':
            if existing:
                form = MaintenanceForm(instance=edit_maintenance)
            else:
                form = MaintenanceForm()
        elif request.method == 'POST':
            if existing:
                form = MaintenanceForm(request.POST, instance=edit_maintenance)
            else:
                form = MaintenanceForm(request.POST)
            if form.is_valid():
                if existing:
                    edited_maintenance = form.save()
                    edited_maintenance.save()
                else:
                    maintenance = form.save(commit=False)
                    maintenance.app = app
                    maintenance.save()
                return render(request, 'message.html', {'message': "Maintenance notes modified Successfully!"})
    else:
        return render(request, 'message.html', {'message': "You are not authorized to view this page!"})
    return render(request, 'maintenance.html', {'form':form})

@login_required
def editDetails(request, num):
    App = apps.get_model('apps', 'App')
    try:
        edit_app = App.objects.get(id=num)
    except:
        return render(request, 'message.html', {'message': "Requested App does not Exist!"})
    editors = edit_app.editors.all()
    if request.user in editors or request.user.is_staff:
        if request.method == 'GET':
            form = EditDetailsForm(instance=edit_app)
        elif request.method == 'POST':
            form = EditDetailsForm(request.POST, instance=edit_app)
            if form.is_valid():
                edited_app = form.save()
                edited_app.save()
                return render(request, 'message.html', {'message': "App Page edited Successfully!"})
    else:
        return render(request, 'message.html', {'message': "You are not authorized to view this page!"})
    return render(request, 'edit_details.html', {'form':form})

@login_required
def modifyDownload(request, num):
    existing = False
    App = apps.get_model('apps', 'App')
    Download = apps.get_model('apps', 'Download')
    Release = apps.get_model('apps', 'Release')
    try:
        app = App.objects.get(id=num)
    except:
        return render(request, 'message.html', {'message': "Requested App does not Exits!"})
    if Download.objects.filter(app=app).exists():
        existing = True
        edit_download = Download.objects.get(app=app)
    if request.user.is_staff or request.user in app.editors.all():
        if request.method == 'GET':
            if existing:
                form = DownloadForm(instance=edit_download)
            else:
                form = DownloadForm()
        elif request.method == 'POST':
            if existing:
                form = DownloadForm(request.POST, instance=edit_download)
            else:
                form = DownloadForm(request.POST)
            if form.is_valid():
                if existing:
                    instance = form.save()
                    release = None
                    releases = Release.objects.filter(app=instance.app)
                    if releases:
                        release = releases.latest('date')
                    choice = instance.download_option
                    link = "https://ns-apps.washington.edu.in/"+instance.app.name+"/#cy-app-instructions-tab"
                    if choice == 'I':
                        instance.download_link = link
                    elif choice == 'D':
                        instance.download_link = release.url
                        if not release:
                            instance.download_link = link
                    elif choice == 'U':
                        instance.download_link = instance.external_url
                        if not instance.external_url:
                            instance.download_link = link
                    if not instance.default_release:
                        instance.default_release = release
                    print instance.download_link
                    instance.save()
                else:
                    download = form.save(commit=False)
                    download.app = app
                    download.save()
                return render(request, 'message.html', {'message': "Instructions modified Successfully!"})
    else:
        return render(request, 'message.html', {'message': "You are not authorized to view this page!"})
    return render(request, 'download.html', {'form':form})
