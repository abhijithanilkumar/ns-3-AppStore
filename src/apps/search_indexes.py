import datetime
from haystack import indexes
from .models import App, Tag


class AppIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    abstract = indexes.CharField(model_attr='abstract')
    description = indexes.CharField(model_attr='description')
    date = indexes.DateTimeField(model_attr='latest_release_date')
    downloads = indexes.IntegerField(model_attr='downloads')
    votes = indexes.IntegerField(model_attr='votes')

    def get_model(self):
        return App

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class TagIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='name')

    def get_model(self):
        return Tag

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
