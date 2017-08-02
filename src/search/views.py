# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.apps import apps
from haystack.query import SearchQuerySet

def findTags():
    min_tag_count = 3
    num_of_top_tags = 20
    tag_cloud_max_font_size_em = 2.0
    tag_cloud_min_font_size_em = 1.0
    tag_cloud_delta_font_size_em = tag_cloud_max_font_size_em - tag_cloud_min_font_size_em

    Tag = apps.get_model('apps', 'Tag')
    top_tags = Tag.objects.all()
    not_top_tags = []

    return top_tags, not_top_tags

def search(request):
    App = apps.get_model('apps', 'App')
    Tag = apps.get_model('apps', 'Tag')
    Author = apps.get_model('apps', 'Author')
    top_tags, not_top_tags = findTags()
    query = request.GET.get('q', '')
    sqs_app = SearchQuerySet()
    sqs_tag = SearchQuerySet()
    sqs_author = SearchQuerySet()
    sqs_app = sqs_app.models(App)
    sqs_tag = sqs_tag.models(Tag)
    sqs_author = sqs_author.models(Author)
    sqs_app = sqs_app.filter(title__contains=query).filter(abstract__contains=query).filter(
        description__contains=query)
    sqs_tag = sqs_tag.filter(title__contains=query)
    sqs_author = sqs_author.filter(title__contains=query).filter(inst__contains=query)
    app = set()
    tag = set()
    author = set()
    for item in sqs_app:
        app.add(item.object)
    for item in sqs_tag:
        tag.add(item.object)
    for item in sqs_author:
        author.add(item.object)
    context = {
        'top_tags': top_tags,
        'not_top_tags': not_top_tags,
        'sqs_app': app,
        'sqs_tag': tag,
        'sqs_author':author,
    }
    return render(request, 'search.html', context)
