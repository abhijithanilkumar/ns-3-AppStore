from django import forms
from models import Comment

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['stars'].label = "How do you rate this page?"
        self.fields['stars'].required = True
        self.fields['title'].required = True
        self.fields['title'].label = "Title"
        self.fields['content'].label = "Comment"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = Comment
        fields = [
            'stars',
            'title',
            'content'
        ]
