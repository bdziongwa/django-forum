from django import forms

from .models import (
    DOMAINS,
    Tag
)

TMP = (
    '1',
    '2'
)


class TopicForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    domain = forms.ChoiceField(choices=DOMAINS)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())


class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class TagForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
