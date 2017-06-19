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
