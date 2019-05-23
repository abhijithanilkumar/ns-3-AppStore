# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from markdownx.models import MarkdownxField
from datetime import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from util.img_util import scale_img

# Create your models here.

class NsRelease(models.Model):
    name = models.CharField(max_length=5)
    url = models.URLField(default="https://www.nsnam.org/ns-3.26/")

    def __str__(self):
        return u'%s-%s' % ("ns", self.name)

    class Meta:
        ordering = ['-name']

class Tag(models.Model):
    identity = models.CharField(max_length=127, editable=False)
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name

    def get_tag_name(self):
        return self.name

class App(models.Model):
    TYPES = [ ('F', 'Fork'),
              ('M', 'Module'),
            ] 
    name = models.CharField(max_length=127, unique=True)
    title = models.CharField(max_length=127, unique=True)
    app_type = models.CharField(max_length=6, choices=TYPES)
    abstract = models.CharField(max_length=255, default="NA")
    description = MarkdownxField()
    icon = models.ImageField(upload_to='app_icon_thumbnail/%Y-%m-%d/', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    editors = models.ManyToManyField(settings.AUTH_USER_MODEL)
    latest_release_date = models.DateField(auto_now_add=True)
    website = models.URLField(blank=True, null=True)
    documentation = models.URLField(blank=True, null=True)
    coderepo = models.URLField(blank=True, null=True)
    contact = models.EmailField(blank=True, null=True)
    active = models.BooleanField(default=False)
    stars = models.PositiveIntegerField(default=0)
    votes = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)
    has_releases = models.BooleanField(default=False)
    issue = models.URLField(blank=True, null=True)
    mailing_list = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def stars_percentage(self):
        return 100 * self.stars / self.votes / 5 if self.votes != 0 else 0

    def update_latest_release_date(self):
        self.latest_release_date = (Release.objects.filter(app=self).latest('date')).date
        self.save()

class Release(models.Model):
    app = models.ForeignKey(App)
    version = models.CharField(max_length=31)
    require = models.ForeignKey(NsRelease, blank=True, null=True)
    date = models.DateField(default=datetime.now, blank=True)
    notes = MarkdownxField()
    filename = models.FileField(upload_to='release_files/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.app.title, self.version)

class Comment(models.Model):
    app = models.ForeignKey(App)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    content = MarkdownxField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment on %s by %s' % (self.app.title, self.user.get_full_name)

class CommentReply(models.Model):
    comment = models.ForeignKey(Comment)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = MarkdownxField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Reply to %s' % (self.comment)

class Screenshot(models.Model):
    app = models.ForeignKey(App)
    screenshot = models.ImageField(upload_to='screenshot/%Y-%m-%d/')
    thumbnail = models.ImageField(upload_to='thumbnail/%Y-%m-%d/')

    def __str__(self):
        return 'Screenshot of %s' % (self.app.title)

class Installation(models.Model):
    app = models.OneToOneField(App)
    installation = MarkdownxField()

    def __str__(self):
        return '%s Installation' % (self.app.title)

    class Meta:
        verbose_name = 'Installation'
        verbose_name_plural = 'Installation Notes'

class Maintenance(models.Model):
    app = models.OneToOneField(App)
    notes = MarkdownxField()

    def __str__(self):
        return '%s Maintenance' % (self.app.title)

    class Meta:
        verbose_name = 'Maintenance'
        verbose_name_plural = 'Maintenance Notes'

class Download(models.Model):
    CHOICES = [('I', 'Point to the Installation tab'),
               ('D', 'Point to the Default Release'),
               ('U', 'Point to a URL of your Choice'),
            ]
    app = models.OneToOneField(App)
    download_option = models.CharField(max_length=1, default='I', choices=CHOICES)
    default_release = models.OneToOneField(Release)
    external_url = models.URLField(blank=True, null=True)
    download_link = models.URLField(editable=False)

    def __str__(self):
        return '%s Download Details' % (self.app.title)

class Development(models.Model):
    app = models.OneToOneField(App)
    notes = MarkdownxField()
    filename = models.FileField(upload_to='release_files/', blank=True, null=True)

    def __str__(self):
        return '%s Development Version' % (self.app.title)

    class Meta:
        verbose_name = 'Development Version'
        verbose_name_plural = 'Development Versions'

@receiver(post_save, sender=Release)
def update_has_releases(sender, instance=None, created=False, **kwargs):
    if created:
        app = instance.app
        app.has_releases = True
        app.save()

@receiver(post_save, sender=Tag)
def update_tag_identity(sender, instance=None, created=False, **kwargs):
    if created:
        instance.identity = instance.name.replace(" ","").lower()
        instance.save()

@receiver(post_save, sender=Download)
def update_download_link(sender, instance=None, created=False, **kwargs):
    if created:
        release = None
        releases = Release.objects.filter(app=instance.app)
        if releases:
            release = releases.latest('date')
        choice = instance.download_option
        link = "http://ns-apps.ee.washington.edu/"+instance.app.name+"/#cy-app-installation-tab"
        if choice == 'I':
            instance.download_link = link
        elif choice == 'D':
            instance.download_link = release.url
            if not release:
                instance.download_link = link
        elif choice == 'U':
            instance.download_link = instance.external_url
            if not instance.external_url:
                instance.download_link = link
        if not instance.default_release:
            instance.default_release = release
        instance.save()

"""
@receiver(post_save, sender=Release)
def update_filename(sender, instance=None, created=False, **kwargs):
    if created:
"""
@receiver(post_save, sender=Screenshot)
def update_thumbnail(sender, instance=None, created=False, **kwargs):
    if created:
        instance.thumbnail = scale_img(instance.screenshot, instance.screenshot.name, 150, 'h')
        instance.save()
