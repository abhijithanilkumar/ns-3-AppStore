from django.views import generic
from django.shortcuts import render
from apps.models import App, Tag
from apps.views import findTags
from apps.forms import SearchFilterForm


def homePage(request):
    new_releases = App.objects.all().filter(
        active=True).order_by('-latest_release_date')[:4]
    top_tags, not_top_tags = findTags()
    form = SearchFilterForm()
    context = {
        'new_releases': new_releases,
        'top_tags': top_tags,
        'not_top_tags': not_top_tags,
        'form': form
    }
    return render(request, 'home.html', context)


class AboutPage(generic.TemplateView):
    template_name = "about.html"

def handler404(request):
    return render(request, '404.html', status=404)