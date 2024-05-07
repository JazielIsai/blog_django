
from django import forms

from blog.posts.models import Publish


class PublishForm(forms.ModelForm):
    class Meta:
        model = Publish
        fields = ['title', 'content', 'image', 'published']


