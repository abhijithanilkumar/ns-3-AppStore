# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from models import App, Release, Tag, Author, Comment
from markdownx.utils import markdownify
from forms import CommentForm

# Create your views here.

def appPage(request, num=0):
    app = get_object_or_404(App, id=num)
    app.description = markdownify(app.description)
    releases = Release.objects.filter(app=app).order_by('-id')
    tags = app.tags.all()
    for release in releases:
        release.notes = markdownify(release.notes)
    authors = app.authors.all()
    if releases:
        latest = releases.latest('id')
    else:
        latest = []
    editors = app.editors.all()
    comments = Comment.objects.filter(app=app)
    return render(request, 'page.html', {'app':app, 'editors':editors, 'tags':tags, 'releases':releases, 'authors':authors, 'latest':latest,
                                         'comments':comments})

def download(request, num):
    app = App.objects.get(id=num)
    releases = Release.objects.filter(app=app).order_by('-id')
    if releases:
        release = releases.latest('id')
        url = release.url
    elif app.coderepo:
        url = app.coderepo
    else:
        url = '/app/'+num
    return redirect(url)

def tagSearch(request, num=0):
    if num:
        try:
            apps = App.objects.filter(tags__id=num)
            active_tag = Tag.objects.get(id=num)
        except:
            return render(request, 'home.html')
        apps_name = apps.order_by('title')
        apps_downloads = apps.order_by('-downloads')
        apps_new = apps.order_by('-latest_release_date')
        apps_votes = apps.order_by('-votes')
        tags = Tag.objects.all()
        return render(request, 'apps_tag.html', {'apps_name':apps_name, 'active_tag':active_tag,
            'apps_downloads':apps_downloads, 'apps_new':apps_new, 'apps_votes':apps_votes, 'tags':tags})
    else:
        apps_name = App.objects.all().order_by('title')
        apps_downloads = App.objects.all().order_by('-downloads')
        apps_new = App.objects.all().order_by('-latest_release_date')
        apps_votes = App.objects.all().order_by('-votes')
        tags = Tag.objects.all()
        return render(request, 'apps.html', {'apps_name':apps_name,
            'apps_downloads':apps_downloads, 'apps_new':apps_new, 'apps_votes':apps_votes, 'tags':tags})

def authorSearch(request, num):
    try:
        apps = App.objects.filter(authors__id=num)
        active_author = Author.objects.get(id=num)
    except:
        return render(request, 'home.html')
    apps_name = apps.order_by('title')
    apps_downloads = apps.order_by('-downloads')
    apps_new = apps.order_by('-latest_release_date')
    apps_votes = apps.order_by('-votes')
    tags = Tag.objects.all()
    return render(request, 'apps_author.html', {'apps_name':apps_name, 'active_author':active_author,
        'apps_downloads':apps_downloads, 'apps_new':apps_new, 'apps_votes':apps_votes, 'tags':tags})

@login_required
def feedback(request, num):
    try:
        app = App.objects.get(id=num)
    except:
        return render(request, 'home.html')
    if request.method == 'GET':
        form = CommentForm()
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.app = app
            comment.user = request.user
            comment.save()
            app.votes += 1
            app.save()
            return render(request, 'message.html', {'message': "Thank you for leaving your Feedback!"})
    return render(request, 'comment.html', {'form':form})
