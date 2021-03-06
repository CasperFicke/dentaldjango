### FORMS.PY THEBLOG APP ###

# Django
from django import forms

# Local
from .models import BlogPost, Category, Comment

# maak list met categorien tbv dropdown
categories = Category.objects.all().values_list('name', 'name')
category_list =[]
for item in categories:
  category_list.append(item)

# Form to add blogpost
class PostForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = ('title', 'header_image', 'title_tag', 'category', 'body', 'snippet')

    widgets = {
      'title'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      #'author'   : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'authorfield', 'type':'hidden'}),
      'category' : forms.Select(choices=category_list, attrs={'class': 'form-control'}),
      'body'     : forms.Textarea(attrs={'class': 'form-control'}),
      'snippet'  : forms.Textarea(attrs={'class': 'form-control'}),
    }

# form to edit blogpost
class UpdateForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = ('title', 'header_image', 'title_tag', 'category', 'body', 'snippet')

    widgets = {
      'title'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'category' : forms.Select(choices=category_list, attrs={'class': 'form-control'}),
      'body'     : forms.Textarea(attrs={'class': 'form-control'}),
      'snippet'  : forms.Textarea(attrs={'class': 'form-control'}),
    }

# Form to add comment
class CommentForm(forms.ModelForm):
  class Meta:
    model  = Comment
    fields = ('name', 'body')

    widgets = {
      'name'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert name here'}),
      'body'     : forms.Textarea(attrs={'class': 'form-control'}),
    }
