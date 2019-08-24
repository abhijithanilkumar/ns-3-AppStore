from django.shortcuts import render, get_object_or_404
from apps.models import App
from download.models import ReleaseDownloadsByDate

def all_stats(request):
    apps = App.objects.filter(active=True)
    context = {
            'apps': apps,
    }
    return render(request, 'all_stats.html', context)


def app_stats(request, name):
    app = get_object_or_404(App, active = True, name = name)
    releases = app.release_set.all()
    app_timeline = dict()
    for r in releases:
        temp = ReleaseDownloadsByDate.objects.filter(release=r).order_by('-when')
        for t in temp:
            app_timeline[t.when] = {}
    
    for r in releases:
        temp = ReleaseDownloadsByDate.objects.filter(release=r)
        for t in temp:
            for re in releases:
                app_timeline[t.when][re.version]=0

    for r in releases:
        temp = ReleaseDownloadsByDate.objects.filter(release=r)
        for t in temp:
            app_timeline[t.when][t.release.version] = 0
            app_timeline[t.when][t.release.version] += t.count

    context = {
            'app': app,
            'app_timeline': app_timeline,
            'releases': releases
    }
    return render(request, 'app_stats.html', context)
