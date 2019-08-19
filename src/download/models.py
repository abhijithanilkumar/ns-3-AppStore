from django.db import models
from apps.models import App, Release
from util.views import ipaddr_long_to_str


class Download(models.Model):
    release = models.ForeignKey(Release, related_name='app_download_stats', on_delete=models.CASCADE)
    when = models.DateField()
    ip4addr = models.PositiveIntegerField()

    def __unicode__(self):
        return unicode(self.release) + u' ' + unicode(self.when) + u' ' + ipaddr_long_to_str(self.ip4addr)


class ReleaseDownloadsByDate(models.Model):
    release = models.ForeignKey(Release, null = True, on_delete=models.CASCADE) # null release has total count across a given day
    when = models.DateField()
    count = models.PositiveIntegerField(default = 0)

    def __unicode__(self):
        return unicode(self.release) + u' ' + unicode(self.when) + u': ' + unicode(self.count)
