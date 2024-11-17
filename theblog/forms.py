from django import forms
from .models import Post

#Define CSS style for Post form (add_post.html) here
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'author', 'body')
    widgets = {
      'title':forms.TextInput(attrs={'class':'form-control'}),
      'author':forms.Select(attrs={'class':'form-control'}),
      'body':forms.Textarea(attrs={'class':'form-control'}),
    }