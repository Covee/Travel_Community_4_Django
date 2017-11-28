from django_countries.widgets import CountrySelectWidget
from django_countries import widgets, countries
from django import forms
from .models import Post, Comment
from django.forms import ModelForm, Textarea


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'country', 'content', 'image',]
        widgets = {'country': CountrySelectWidget(),
                   'content': Textarea(attrs={'class': 'form-control' })
            }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'country', 'content', 'image',]
        widgets = {'country': CountrySelectWidget(),
                   'content': Textarea(attrs={'class': 'form-control' })
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'message')

    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )


    
