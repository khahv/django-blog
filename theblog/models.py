from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# from ckeditor.fields import RichTextField
from froala_editor.fields import FroalaField

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('home')
  
class MachineTemplate(models.Model):
  name = models.CharField(max_length=255)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('home')

class Post(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  # body  = models.TextField()
  body = FroalaField(blank=True, null=True)
  # body = RichTextField(blank=True, null=True)
  post_date = models.DateField(auto_now_add=True)
  # category = models.CharField(max_length=255, default='coding')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  machines = models.ManyToManyField(MachineTemplate, blank=True) 
  
  def __str__(self):
    return self.title + '|' + str(self.author)
  def get_absolute_url(self):
    return reverse('article-detail', args=(str(self.id)))

