# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.apps import apps
from haystack.query import SearchQuerySet

# Create your views here.
def search(request):
    App = apps.get_model('apps', 'App')
    Tag = apps.get_model('apps', 'Tag')
    Author = apps.get_model('apps', 'Author')
    tags = Tag.objects.all()
    query = request.GET.get('q', '')
    sqs_app = SearchQuerySet()
    sqs_tag = SearchQuerySet()
    sqs_author = SearchQuerySet()
    sqs_app = sqs_app.models(App)
    sqs_tag = sqs_tag.models(Tag)
    sqs_author = sqs_author.models(Author)
    sqs_app = sqs_app.filter(title__contains=query).filter(abstract__contains=query).filter(description__contains=query)
    sqs_app_name = sqs_app.order_by('title')
    sqs_app_downloads = sqs_app.order_by('-downloads')
    sqs_app_new = sqs_app.order_by('-date')
    sqs_app_votes = sqs_app.order_by('-votes')
    sqs_tag = sqs_tag.filter(title__contains=query)
    sqs_author = sqs_author.filter(title__contains=query).filter(inst__contains=query)
    return render(request, 'search.html', {'tags':tags, 'sqs_app_name':sqs_app_name, 'sqs_tag':sqs_tag, 'sqs_author':sqs_author,
        'sqs_app_downloads':sqs_app_downloads, 'sqs_app_votes':sqs_app_votes, 'sqs_app_new':sqs_app_new})
