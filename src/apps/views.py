# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from models import App, Release, Tag, Author, Comment, Screenshot
from markdownx.utils import markdownify
from forms import CommentForm

# Create your views here.

def findTags():
    min_tag_count = 3
    num_of_top_tags = 20
    tag_cloud_max_font_size_em = 2.0
    tag_cloud_min_font_size_em = 1.0
    tag_cloud_delta_font_size_em = tag_cloud_max_font_size_em - tag_cloud_min_font_size_em

    top_tags = Tag.objects.all()
    not_top_tags = []

    return top_tags, not_top_tags

def appPage(request, name):
    app = get_object_or_404(App, name=name)
    app.description = markdownify(app.description)
    releases = Release.objects.filter(app=app).order_by('-id')
    tags = app.tags.all()
    screenshots = Screenshot.objects.filter(app=app)
    for release in releases:
        release.notes = markdownify(release.notes)
    authors = app.authors.all()
    if releases:
        latest = releases.latest('date')
    else:
        latest = []
    editors = app.editors.all()
    comments = Comment.objects.filter(app=app)
    go_back_to_url = "/"
    go_back_to_title = "home"
    context = {
        'app':app,
        'editors':editors,
        'tags':tags,
        'releases':releases,
        'screenshots':screenshots,
        'authors':authors,
        'latest':latest,
        #'comments':comments,
        'go_back_to_url':go_back_to_url,
        'go_back_to_title':go_back_to_title,
    }
    return render(request, 'page.html', context)

def download(request, num):
    app = App.objects.get(id=num)
    releases = Release.objects.filter(app=app).order_by('-id')
    bake = 0
    code = 0
    website = 0
    if releases:
        release = releases.latest('date')
        bake = release.filename
    if app.coderepo:
        code = app.coderepo
    if app.website:
        website = app.website
    context = {
        'bake':bake,
        'code':code,
        'website':website,
    }
    return render(request, 'download.html', context)

def tagSearch(request, name):
    if num:
        try:
            apps = App.objects.filter(tags__identity=name).filter(active=True)
            active_tag = Tag.objects.get(identity=name)
        except:
            return render(request, 'home.html')
        top_tags, not_top_tags = findTags()
        context = {
            'apps':apps,
            'top_tags':top_tags,
            'not_top_tags':not_top_tags,
            'tag':active_tag,
            'selected_tag_name':active_tag.name,
        }
        return render(request, 'apps_tag.html', context)
    else:
        apps = App.objects.all().order_by('title')
        top_tags, not_top_tags = findTags()
        context = {
            'apps':apps,
            'top_tags':top_tags,
            'not_top_tags':not_top_tags,
            'navbar_selected_link':"all",
        }
        return render(request, 'apps.html', context)

def authorSearch(request, name):
    try:
        apps = App.objects.filter(authors__identity=name).filter(active=True)
        active_author = Author.objects.get(identity=name)
    except:
        return render(request, 'home.html')
    apps_name = apps.order_by('title')
    top_tags, not_top_tags = findTags()
    context = {
        'apps':apps,
        'top_tags':top_tags,
        'not_top_tags':not_top_tags,
        'author_name':active_author.name,
    }
    return render(request, 'apps_author.html', context)

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
