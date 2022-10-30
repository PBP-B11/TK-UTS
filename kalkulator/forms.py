from django import forms
from kalkulator.models import Kalkulator
class addHistory(forms.Form):
    class Meta:
        model = Kalkulator
        electricity = forms.IntegerField()
        offset =  forms.IntegerField()
        envfactor = forms.IntegerField()
        roofarea = forms.IntegerField()
        date = forms.IntegerField()   
         #size estimate sama panel ga dimasukin ke forms, soalnya itu output