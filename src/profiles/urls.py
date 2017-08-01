from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^myapps$', views.userLanding, name='user_landing'),
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),
        name='show'),
]
