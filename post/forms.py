from django.forms import ModelForm
from .models import Question

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id']

class Comment(ModelForm):
    class Meta:
        model = Post
        exclude = ['id']
