# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from models import App
from models import NsRelease
from models import Tag
from models import Release
import datetime

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

class ReleaseTestCase(TestCase):
    def setUp(self):
        App.objects.create(name='App2',
                           title='App Title',
                           app_type='F',
                           abstract='This is a test App for Release',
                           description='This is a test App for Release')
        NsRelease.objects.create(name='NsR2',
                                 url='https://www.nsnam.org/ns-3.29/')
        release_app = App.objects.get(name='App2')
        release_nsrelease = NsRelease.objects.get(name='NsR2')
        Release.objects.create(app=release_app,
                               version='0.1',
                               require=release_nsrelease,
                               date=datetime.date(2018,10,25),
                               notes='## usage \n This is a test Markdown text',
                               filename=SimpleUploadedFile('release.test',str('Test me')),
                               url='https://www.nsnam.org/ns-3.29/')
    def test_release_created(self):
        release = Release.objects.get(app__name="App2",
                                      require__name="NsR2")
        self.assertTrue(isinstance(release, Release))
        self.assertTrue(release.app.title, 'App Title')
        self.assertTrue(release.app.app_type, 'F')
        self.assertTrue(release.app.abstract, 'This is a test App for Release')
        self.assertTrue(release.app.description, 'This is a test App for Release')
        self.assertTrue(release.require.url, 'https://www.nsnam.org/ns-3.29/')
        self.assertTrue(release.date, datetime.date(2018,10,25))
        self.assertTrue(release.notes, '## usage \n This is a test Markdown text')
        self.assertTrue(release.filename.name, 'release.test')
        release_file = open(release.filename.url[1:], "r")
        self.assertTrue(release_file.read(), 'Test me')
        release_file.close()
        self.assertTrue(release.url, 'https://www.nsnam.org/ns-3.29/')
        