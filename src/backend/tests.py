# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from models import App
from models import Tag
import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

class AppTestCase(TestCase):
    def setUp(self):
        self.test_image = b"GIF89a\x10\x00\x10\x00\xf6d\x00\xeb\xbb\x18\xeb\xbe!\xf3\xc1\x1a\xfa\xc7\x19\xfd\xcb\x1b\xff\xcc\x1c\xeb\xc2*\xff\xcf#\xff\xcf$\xff\xd0%\xff\xd0&\xff\xd3-\xfd\xd2/\xff\xd3.\xff\xd3/\xeb\xc54\xe8\xc7=\xff\xd30\xff\xd40\xfd\xd56\xff\xd67\xfa\xd39\xff\xd78\xff\xd79\xff\xd7:\xf9\xd5>\xff\xd8:\xec\xceE\xfd\xd9A\xff\xdaA\xff\xdaB\xff\xdbB\xff\xdbC\xff\xdbD\xfd\xddJ\xff\xdeK\xff\xdfM\xfd\xdeN\xff\xdfN\xff\xe2U\xff\xe3W\xff\xe3X\xff\xe6a\xff\xe7a\xff\xe7b\xf2\xe1n\xf5\xe3o\xfd\xe9j\xff\xebl2`\x876f\x906g\x915h\x926i\x936i\x947h\x967j\x969l\x968l\x979m\x99:o\x9b:p\x9c;p\x9c;p\x9d<q\x9e=s\xa0=s\xa2=t\xa1>t\xa2>u\xa3?v\xa5@x\xa6@x\xa7Ay\xa8B{\xaaC|\xabC}\xadC}\xaeD}\xadD~\xadE\x7f\xafF\x80\xb0F\x80\xb1F\x81\xb2G\x81\xb2H\x83\xb4H\x84\xb5H\x85\xb6I\x85\xb7J\x87\xb9J\x86\xbaK\x88\xbbL\x89\xbcL\x8a\xbcM\x8b\xbeL\x8a\xbfN\x8d\xc0O\x8d\xc1P\x8f\xc3R\x91\xc6\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\xf9\x04\x01\x00\x00e\x00,\x00\x00\x00\x00\x10\x00\x10\x00\x00\x07\xa6\x80e\x82eaZRLF@7\x83\x8c\x82]dRJD=8\x8d\x8cW\x91D>85\x96e_WLD9298\x95\x8cca\\UPG@<5\xa7e'#\x19eb_TPJ\xb05\xbf1e#\x1d\x13\x9fWT\x92@\xa74\xc1\x1b\xc4\x0be\xc7KG\x9d\x8d\x1d\x17\x0b\x07eR\xd34e-/,'&!\xd8\x08\x04eLJCe.0,)\xe4\xe6\x05\x02\x82C>e\xef\xf1\x1d\x1a\x0b\x08\x05\x05,\xc13\x01\xe1\x81\x81\x00\x00\x00x\x8aW.B\x82\x80\x9e\xca\xc8\x93\x90\x80\x0c\xba\x88e*8,0\x00\xa3\xc7A\x81\x00\x00;"
        editors, tags = [] , []

        User = get_user_model()
        editors.append(User.objects.create(email='developer1@ml.lm',
                                           password='developer1pass'))
        editors.append(User.objects.create(email='developer2@ml.lm',
                                           password='developer2pass'))
        tags.append(Tag.objects.create(identity='tag1-identity',
                                       name='tag1'))
        tags.append(Tag.objects.create(identity='tag2-identity',
                                       name='tag2'))
        test_App = App.objects.create(name='App1',
                                      title='App Title',
                                      app_type='F',
                                      abstract='This is a test App',
                                      description='This is a test App',
                                      icon=SimpleUploadedFile('test_image.gif', self.test_image, content_type='image/gif'),
                                      latest_release_date=datetime.date(2018,10,31),
                                      website='http://test.website.app',
                                      documentation='http://test.website.app/docs',
                                      coderepo='http://vcontrol-hub.com/my-app',
                                      contact='developer@mailservice.com',
                                      active=True,
                                      stars=4,
                                      votes=3,
                                      downloads=1,
                                      has_releases=True,
                                      issue='http://test.website.app/bugzilla',
                                      mailing_list='http://mailman-testapp.com/test-app-developer/',)
        for editor in editors:
            editor.save()
            test_App.editors.add(editor)
        for tag in tags:
            tag.save()
            test_App.tags.add(tag)
    def test_app_created(self):
        app = App.objects.get(name='App1')
        self.assertTrue(isinstance(app, App))
        self.assertEqual(app.title, 'App Title')
        self.assertEqual(app.app_type, 'F')
        self.assertEqual(app.abstract, 'This is a test App')
        self.assertEqual(app.description, 'This is a test App')
        f = open(app.icon.url[1:], 'rb')
        self.assertEqual(f.read(), self.test_image)
        f.close()
        self.assertEqual(app.latest_release_date, datetime.date(2018,10,31))
        self.assertEqual(app.website, 'http://test.website.app')
        self.assertEqual(app.documentation, 'http://test.website.app/docs')
        self.assertEqual(app.coderepo, 'http://vcontrol-hub.com/my-app')
        self.assertEqual(app.contact, 'developer@mailservice.com')
        self.assertEqual(app.active, True)
        self.assertEqual(app.stars, 4)
        self.assertEqual(app.votes, 3)
        self.assertEqual(app.downloads, 1)
        self.assertEqual(app.has_releases, True)
        self.assertEqual(app.issue, 'http://test.website.app/bugzilla')
        self.assertEqual(app.mailing_list, 'http://mailman-testapp.com/test-app-developer/')
        devs = app.editors.all()
        self.assertEqual(len(devs), 2)
        self.assertEqual(devs[0].email, 'developer1@ml.lm')
        self.assertEqual(devs[1].email, 'developer2@ml.lm')
        self.assertEqual(devs[0].password, 'developer1pass')
        self.assertEqual(devs[1].password, 'developer2pass')
        tags = app.tags.all()
        self.assertEqual(len(tags), 2)
        self.assertEqual(tags[0].name, 'tag1')
        self.assertEqual(tags[1].name, 'tag2')
