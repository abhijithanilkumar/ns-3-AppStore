from django import forms
from .models import Comment, Tag, App


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['title'].label = "Title"
        self.fields['content'].label = "Comment"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = Comment
        fields = [
            'title',
            'content'
        ]


# This form can be used to take inputs from the User and filter the search results.
# The code is not in use right now, as we do not accept User inputs for filtering.
# The form can be enhanced to accept more fields and filter based on it in
# the future, if required.
class SearchFilterForm(forms.Form):
    tag = forms.ModelChoiceField(
        label="Select the Tag",
        required=False,
        queryset=Tag.objects.all())
    app_type = forms.ChoiceField(
        label="Select the type of App",
        required=False,
        choices=App.TYPES)

    def clean(self):
        return self.cleaned_data
