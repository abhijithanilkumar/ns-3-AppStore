from django import forms
from models import Comment

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['stars'].label = "How do you rate this page?"
        self.fields['stars'].required = True
        self.fields['content'].label = "Leave a Comment"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = Comment
        fields = [
            'stars',
            'content'
        ]
