# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import App, Release, Tag, Comment, Screenshot, Download
from markdownx.utils import markdownify
from .forms import CommentForm
from django.http import HttpResponseRedirect

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
    if name == "inactive":
        apps = App.objects.all().filter(active=False).order_by('title')
        top_tags, not_top_tags = findTags()
        context = {
            'apps':apps,
            'top_tags':top_tags,
            'not_top_tags':not_top_tags,
        }
        return render(request, 'apps.html', context)
    else:
        app = get_object_or_404(App, name=name)
        if request.method == 'POST':
            rating_n = request.POST.get('rating')
            try:
                rating_n = int(rating_n)
                if not (0 <= rating_n <= 5):
                    raise ValueError()
            except ValueError:
                raise ValueError('rating is "%s" but must be an integer between 0 and 5' % rating_n)
            app.votes += 1
            app.stars += rating_n
            app.save()
            return HttpResponseRedirect('/app/'+app.name)
        if request.method == 'GET':
            app.description = markdownify(app.description)
            releases = Release.objects.filter(app=app).order_by('-id')
            tags = app.tags.all()
            screenshots = Screenshot.objects.filter(app=app)
            for release in releases:
                release.notes = markdownify(release.notes)
            download = Download.objects.filter(app=app)
            if download:
                latest = app.download.default_release
            else:
                latest = None
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
                'latest':latest,
                #'comments':comments,
                'go_back_to_url':go_back_to_url,
                'go_back_to_title':go_back_to_title,
            }
            return render(request, 'page.html', context)

def tagSearch(request, name="all"):
    if name != "all":
        try:
            apps = App.objects.filter(tags__identity=name).filter(active=True)
            active_tag = Tag.objects.get(identity=name)
        except:
            return render(request, 'message.html')
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
        apps = App.objects.all().filter(active=True).order_by('title')
        top_tags, not_top_tags = findTags()
        context = {
            'apps':apps,
            'top_tags':top_tags,
            'not_top_tags':not_top_tags,
            'navbar_selected_link':"all",
        }
        return render(request, 'apps.html', context)

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
