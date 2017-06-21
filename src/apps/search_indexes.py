import datetime
from haystack import indexes
from models import App, Tag

class AppIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.NgramField(model_attr='title')

    def get_model(self):
        return App

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class TagIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Tag

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
