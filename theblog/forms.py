from django import forms
from .models import BlogPost


# Form to add blogpost
class PostForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = ('title', 'title_tag', 'author','body')

    widgets = {
      'title'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      # 'author'   : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'authorfield', 'type':'hidden'}),
      'author' : forms.Select(attrs={'class': 'form-control'}),
      #'category' : forms.Select(choices=categorien_list, attrs={'class': 'form-control'}),
      'body'     : forms.Textarea(attrs={'class': 'form-control'}),
      #'snippet'  : forms.Textarea(attrs={'class': 'form-control'}),
    }

# form to edit blogpost
class UpdateForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = ('title', 'title_tag', 'body')

    widgets = {
      'title'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'body'     : forms.Textarea(attrs={'class': 'form-control'}),
      # 'snippet'  : forms.Textarea(attrs={'class': 'form-control'}),
    }
