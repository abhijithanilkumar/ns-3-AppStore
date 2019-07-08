from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'apps'

urlpatterns = [
    # path('tag/', views.tagSearch, name='tagSearch'),
    path('<slug:name>/', views.appPage, name='appPage'),
    path('tag/all/', views.tagSearch, name='allApps'),
    path('tag/<slug:name>/', views.tagSearch, name='tagSearch'),
    path('feedback/<int:num>/', views.feedback, name='feedback'),
]
