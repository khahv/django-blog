from django import forms
from .models import Post, Category
from froala_editor.widgets import FroalaEditor

# choices = [('Coding','Coding'),('Linux','Linux'),('Windows','Windows')]
# choices = Category.objects.all().values_list('name','name')
# choice_list = []

# for item in choices:
#     choice_list.append(item)

#Define CSS style for Post form (add_post.html) here
class PostForm(forms.ModelForm):
  body = forms.CharField(widget=FroalaEditor)  # Gắn FroalaEditor vào trường "content"

  class Meta:
    model = Post
    fields = ('title', 'author', 'category', 'body')
    widgets = {
      'title':forms.TextInput(attrs={'class':'form-control'}),
      'author':forms.Select(attrs={'class':'form-control'}),
      'category':forms.Select(attrs={'class':'form-control'}),
      'body':forms.Textarea(attrs={'class':'form-control'}),
    }