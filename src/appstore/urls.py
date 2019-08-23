from django.conf.urls import include, url
from django.urls import path
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
    path('', views.homePage, name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('users/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', include('accounts.urls', namespace='accounts')),
    path('app/', include('apps.urls', namespace='apps')),
    path('search/', include('search.urls', namespace='search')),
    path('backend/', include('backend.urls', namespace='edit')),
    path('download/', include('download.urls', namespace='download')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
