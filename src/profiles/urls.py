from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('myapps', views.userLanding, name='user_landing'),
    path('me', views.ShowProfile.as_view(), name='show_self'),
    path('me/edit', views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),
        name='show'),
]
