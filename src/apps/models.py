# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    institution = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if not self.institution:
            return self.name
        else:
            return u'%s (%s)' % (self.name, self.institution)

class App(models.Model):
    title = models.CharField(max_length=127, unique=True)
    abstract = models.CharField(max_length=255)
    description = MarkdownxField()
    authors      = models.ManyToManyField(Author, blank=True, through='OrderedAuthor')
    editors      = models.ManyToManyField(User, blank=True)
    latest_release_date       = models.DateField(blank=True, null=True)
    website      = models.URLField(blank=True, null=True)
    tutorial     = models.URLField(blank=True, null=True)
    coderepo     = models.URLField(blank=True, null=True)
    contact      = models.EmailField(blank=True, null=True)
    stars        = models.PositiveIntegerField(default=0)
    votes        = models.PositiveIntegerField(default=0)
    downloads    = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
