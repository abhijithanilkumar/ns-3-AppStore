from django.views import generic
from django.shortcuts import render
from apps.models import App, Tag

def homePage(request):
    new_releases = App.objects.all().order_by('-latest_release_date')[:4]
    top_downloaded = App.objects.all().order_by('-downloads')[:4]
    tags = Tag.objects.all()
    return render(request, 'home.html', {'new_releases':new_releases, 'top_downloaded':top_downloaded, 'tags':tags})


class AboutPage(generic.TemplateView):
    template_name = "about.html"
