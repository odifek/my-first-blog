from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form for posting whatever we want """

    class Meta:
        model = Post
        fields = ('title', 'text')
