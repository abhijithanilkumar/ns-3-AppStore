from django import forms
from django.apps import apps
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

class CreateAppForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['title'].required = True
        self.fields['editors'].required = True
        self.fields['description'].label = "Description (Markdown Supported)"

        self.helper.layout = Layout(
            Field('title', placeholder="Title of the App", autofocus=""),
            Field('editors', placeholder="Editors of the App"),
            Field('abstract', placeholder="App Abstract (fill dummy data if the abstract is not available)"),
            Field('description', placeholder="App Details (fill dummy data if the description is not available)"),
            Submit('create', 'Create New Page',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

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
        self.fields['active'].label = "Tick to make the App Active (Appear in the main page)"

        self.helper.layout = Layout(
            Field('title', placeholder="Title of the App", autofocus=""),
            Field('editors', placeholder="Editors of the App"),
            Field('abstract', placeholder="App Abstract (fill dummy data if the abstract is not available)"),
            Field('description', placeholder="App Details (fill dummy data if the description is not available)"),
            Field('icon', placeholder="App Icon"),
            Field('tags', placeholder="Choose the App Tags"),
            Field('website', placeholder="eg : https://www.nsnam.org"),
            Field('documentation', placeholder="Link to documentation/tutorial"),
            Field('mailing_list', placeholder="Link to the mailing list"),
            Field('issue', placeholder="Link to the issue tracker"),
            Field('coderepo', placeholder="Link to the Source code"),
            Field('contact', placeholder="Email ID of the maintainer"),
            Field('active'),
            Submit('edit', 'Submit',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

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
        self.helper = FormHelper()
        self.fields['description'].label = "Details (Markdown Supported)"

        self.helper.layout = Layout(
            Field('description', placeholder="App Details", autofocus=""),
            Submit('details', 'Submit',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

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
        self.helper = FormHelper()
        self.fields['version'].label = "Version"
        self.fields['version'].required = True
        self.fields['require'].label = "Requires ns-3 Version"
        self.fields['require'].required = True
        self.fields['notes'].label = "Release Notes (Markdown Supported)"
        self.fields['filename'].label = "Release File (bakeconf.xml)"
        self.fields['url'].label = "Release Url"

        self.helper.layout = Layout(
            Field('version', placeholder="Release Version", autofocus=""),
            Field('require',),
            Field('notes', placeholder="Release Notes"),
            Field('filename',),
            Field('url', placeholder="URL that points to the latest release"),
            Submit('release', 'Submit',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'Release')
        exclude = [
            'app',
        ]

class InstallationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['installation'].label = "Installation instructions (Markdown Supported)"

        self.helper.layout = Layout(
            Field('installation', placeholder="Installation Instructions", autofocus=""),
            Submit('release', 'Submit',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'Installation')
        exclude = [
            'app',
        ]

class MaintenanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['notes'].label = "Maintenance Notes (Markdown Supported)"

        self.helper.layout = Layout(
            Field('notes', placeholder="Maintenance Notes", autofocus=""),
            Submit('maintenance', 'Submit',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'Maintenance')
        exclude = [
            'app',
        ]

class DownloadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['download_option'].label = "Download Button Points to"
        self.fields['default_release'].label = "Default Release"
        self.fields['external_url'].label = "External Download URL"

        self.helper.layout = Layout(
            Field('download_option', placeholder="Download Button Points to", autofocus=""),
            Field('default_release', placeholder="Default release for the App"),
            Field('external_url', placeholder="eg: Link to a .tar file"),
            Submit('maintenance', 'Submit',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = apps.get_model('apps', 'Download')
        exclude = [
            'app',
            'download_link',
        ]
