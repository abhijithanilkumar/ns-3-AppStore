# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from models import App


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
