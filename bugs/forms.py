from django import forms
from .models import Bugs


class BugForm(forms.ModelForm):
    class Meta:
        model = Bugs
        fields = ('title', 'content', 'image', 'tag')
