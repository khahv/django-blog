from django import forms
from .models import Post, Category, MachineTemplate
from froala_editor.widgets import FroalaEditor
from django_select2.forms import Select2MultipleWidget
# choices = [('Coding','Coding'),('Linux','Linux'),('Windows','Windows')]
# choices = Category.objects.all().values_list('name','name')
# choice_list = []

# for item in choices:
#     choice_list.append(item)

#Define CSS style for Post form (add_post.html) here
class PostForm(forms.ModelForm):
  body = forms.CharField(widget=FroalaEditor)  

  class Meta:
    model = Post
    fields = ('title', 'author', 'category', 'machines', 'body')
    widgets = {
      'title':forms.TextInput(attrs={'class':'form-control'}),
      'author':forms.Select(attrs={'class':'form-control'}),
      'category':forms.Select(attrs={'class':'form-control'}),
      'machines':Select2MultipleWidget,
      'body':forms.Textarea(attrs={'class':'form-control'}),
    }