import datetime
from haystack import indexes
from models import App

class AppIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(documet=True, use_template=True)

    def get_model(self):
        return App

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(latest_release_date__lte=datetime.date.today())
