from django import forms
from django.apps import apps

class CreateAppForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Title *"
        self.fields['abstract'].label = "Abstract (255 characters) *"
        self.fields['description'].label = "Description (Markdown Supported!) *"
        self.fields['authors'].label = "Authors of the App"
        self.fields['editors'].label = "Editors (Users with Edit Previlege)"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'App')
        fields = [
            'title',
            'abstract',
            'description',
            'authors',
            'editors',
        ]

class EditAppForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Title *"
        self.fields['abstract'].label = "Abstract (255 characters) *"
        self.fields['description'].label = "Description (Markdown Supported!) *"
        self.fields['authors'].label = "Authors of the App"
        self.fields['tags'].label = "Tags related to the App"
        self.fields['website'].label = "Website of the App"
        self.fields['tutorial'].label = "Tutorial Website Link"
        self.fields['coderepo'].label = "Link to the Code Repository"
        self.fields['contact'].label = "Contact Email"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'App')
        exclude = [
            'editors',
            'stars',
            'votes',
            'downloads',
        ]

class ReleaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['version'].label = "Version *"
        self.fields['require'].label = "Requires ns-3 Version *"
        self.fields['notes'].label = "Release Notes *"
        self.fields['dependencies'].label = "Package Dependencies *"
        self.fields['filename'].label = "Release File (bakeconf.xml)"
        self.fields['url'].label = "Release Url"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'Release')
        exclude = [
            'app',
            'date',
        ]
