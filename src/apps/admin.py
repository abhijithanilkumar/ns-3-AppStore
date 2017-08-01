# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Tag, App, Release, NsRelease, Comment, Screenshot, \
        Maintenance, Installation, Download, Development

# Register your models here.
admin.site.register(Tag)
admin.site.register(App)
admin.site.register(Release)
admin.site.register(NsRelease)
admin.site.register(Comment)
admin.site.register(Screenshot)
admin.site.register(Maintenance)
admin.site.register(Installation)
admin.site.register(Download)
admin.site.register(Development)
