from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    model = Post
    fields = ('author', 'title', 'text')

    widgets = {
        'title':form.TextInput(attrs={'class':'textinputclass'}),
        'text':form.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
    }

class CommentForm(forms.ModelForm):
    model = Comment
    fields = ('auther', 'text')

    widgets = {
        'author': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
    }
