from django import forms
from django.forms import ModelForm, TextInput, URLInput
from artikel.models import Artikel

class addArticle(ModelForm) :
    class Meta:
            model = Artikel
            fields = ['title', 'url','gambar']
            widgets = {
                'title': TextInput(attrs={
                    'id': "title",
                    'class': "form-control",
                    'placeholder': 'Title'
                    }),
                'url': URLInput(attrs={
                    'id':'url',
                    'class': "form-control", 
                    'placeholder': 'Article URL'
                    }),
                'gambar': URLInput(attrs={
                    'id':'gambar',
                    'class': "form-control", 
                    'placeholder': 'Image URL'
                    })
            }

    