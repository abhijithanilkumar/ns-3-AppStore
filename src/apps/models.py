# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from markdownx.models import MarkdownxField
import datetime

# Create your models here.

class NsRelease(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self):
        return u'%s-%s' % ("ns", self.name)

class Author(models.Model):
    name = models.CharField(max_length=50)
    institution = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if not self.institution:
            return self.name
        else:
            return u'%s (%s)' % (self.name, self.institution)

class Tag(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name

    def get_tag_name(self):
        return self.name

class App(models.Model):
    title = models.CharField(max_length=127, unique=True)
    abstract = models.CharField(max_length=255, default="NA")
    description = MarkdownxField()
    icon = models.ImageField(upload_to='app_icon_thumbnail/%Y-%m-%d/', blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    editors = models.ManyToManyField(settings.AUTH_USER_MODEL)
    latest_release_date = models.DateField(auto_now_add=True)
    website = models.URLField(blank=True, null=True)
    tutorial = models.URLField(blank=True, null=True)
    coderepo = models.URLField(blank=True, null=True)
    contact = models.EmailField(blank=True, null=True)
    stars = models.PositiveIntegerField(default=0)
    votes = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Release(models.Model):
    app = models.ForeignKey(App)
    version = models.CharField(max_length=31)
    require = models.ForeignKey(NsRelease)
    date = models.DateField(auto_now_add=True)
    notes = MarkdownxField()
    dependencies = models.ManyToManyField('self', related_name='dependents', symmetrical='False', blank=True, null=True)
    filename = models.FileField(upload_to='release_files/%Y-%m-%d/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.app.title, self.version)

class Comment(models.Model):
    CHOICES = [
        (1, 'Not Useful'),
        (2, 'Needs Improvement'),
        (3, 'Okay'),
        (4, 'Great'),
        (5, 'Awesome'),
    ]

    app = models.ForeignKey(App)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    stars = models.PositiveIntegerField(choices=CHOICES)
    content = MarkdownxField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment on %s by %s' % (self.app.title, self.user.get_full_name)
