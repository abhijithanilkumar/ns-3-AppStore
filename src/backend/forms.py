from django import forms
from django.apps import apps
from crispy_forms.helper import FormHelper

class CreateAppForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Title"
        self.fields['title'].required = True
        self.fields['editors'].label = "Editors (Users with Edit Previlege)"
        self.fields['editors'].required = True

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'App')
        fields = [
            'title',
            'abstract',
            'description',
            'editors',
        ]

class EditAppForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['title'].label = "Title"
        self.fields['title'].required = True
        self.fields['abstract'].label = "Abstract (255 characters)"
        self.fields['abstract'].required = True
        self.fields['description'].label = "Description (Markdown Supported!)"
        self.fields['icon'].label = "App Icon"
        self.fields['tags'].label = "Tags related to the App"
        self.fields['website'].label = "Website of the App"
        self.fields['documentation'].label = "Tutorial Website Link"
        self.fields['mailing_list'].label = "Module Mailing List"
        self.fields['issue'].label = "Module Issue Tracker"
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
            'has_releases',
        ]

class EditDetailsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['description'].label = "Details (Markdown Supported)"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'App')
        fields = [
            'description'
        ]

class ReleaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['version'].label = "Version"
        self.fields['version'].required = True
        self.fields['require'].label = "Requires ns-3 Version"
        self.fields['require'].required = True
        self.fields['notes'].label = "Release Notes"
        self.fields['filename'].label = "Release File (bakeconf.xml)"
        self.fields['url'].label = "Release Url"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'Release')
        exclude = [
            'app',
        ]

class InstructionsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['default_release'].label = "Default Release"
        self.fields['installation'].label = "Installation instructions (Markdown Supported)"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'Instructions')
        exclude = [
            'app',
        ]

class MaintenanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['notes'].label = "Maintenance notes (Markdown Supported)"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'Maintenance')
        exclude = [
            'app',
        ]
