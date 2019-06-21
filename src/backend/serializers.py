from rest_framework import serializers
from apps.models import App as AppModel, Release

class App(object):
    def __init__(
            self,
            name=None,
            app_type=None,
            coderepo=None,
            version=None,
            message=None,
            ns=None,
            bakefile_url=None):
        self.name = name
        self.app_type = app_type
        self.coderepo = coderepo
        self.version = version
        self.ns = ns
        self.bakefile_url = bakefile_url
        self.message = message


class AppSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=127)
    app_type = serializers.CharField(max_length=1)
    coderepo = serializers.URLField()
    version = serializers.CharField(max_length=31)
    ns = serializers.CharField(max_length=5)
    bakefile_url = serializers.CharField(max_length=255)
    message = serializers.CharField(max_length=255)


class AppSearch(object):
    def __init__(
            self,
            name=None,
            version=None,
            title=None,
            abstract=None
        ):
        self.name = name
        self.version = version
        self.title = title
        self.abstract = abstract


class AppSearchSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.CharField(max_length=127)
    # version = serializers.CharField(max_length=31)
    # title = serializers.CharField(max_length=127)
    # abstract = serializers.CharField(max_length=255)
    class Meta:
        model = AppModel
        fields = ('name', 'title', 'abstract')