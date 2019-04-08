from django import forms
from .models import Bugs, Comments


class BugForm(forms.ModelForm):
    class Meta:
        model = Bugs
        fields = ('title', 'content', 'image', 'tag')


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': '5', 'cols': '5'})
    )

    class Meta:
        model = Comments
        fields = ['comment']
