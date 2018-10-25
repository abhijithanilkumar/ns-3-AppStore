# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from models import App
from models import NsRelease
from models import Tag

class AppTestCase(TestCase):
    def setUp(self):
        App.objects.create(name='App1',
                           title='App Title',
                           app_type='F',
                           abstract='This is a test App',
                           description='This is a test App')
    def test_app_created(self):
        app = App.objects.get(name='App1')
        self.assertTrue(isinstance(app, App))
        self.assertEqual(app.title, 'App Title')

class NsReleaseTestCase(TestCase):
    def setUp(self):
        NsRelease.objects.create(name='NsR1',
                                 url='https://www.nsnam.org/ns-3.29/')
    def test_nsrelease_created(self):
        nsrelease = NsRelease.objects.get(name='NsR1')
        self.assertTrue(isinstance(nsrelease, NsRelease))
        self.assertEqual(nsrelease.url, 'https://www.nsnam.org/ns-3.29/')

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(identity='This is a test Tag',
                           name='Tag1')
    def test_tag_created(self):
        tag = Tag.objects.get(name='Tag1')
        self.assertTrue(isinstance(tag, Tag))
        self.assertEqual(tag.name, 'Tag1')