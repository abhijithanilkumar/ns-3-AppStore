from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import apps.urls
import search.urls
import backend.urls
from . import views

urlpatterns = [
    url(r'^$', views.homePage, name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^app/', include(apps.urls, namespace='apps')),
    url(r'^search/', include(search.urls, namespace='search')),
    url(r'^backend/', include(backend.urls, namespace='edit')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
