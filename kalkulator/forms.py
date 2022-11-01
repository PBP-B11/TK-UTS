from django import forms
from kalkulator.models import Calculation
class AddHistory(forms.Form):
    model = Calculation
    electricity = forms.IntegerField(label="")
    offset = forms.IntegerField(label="")
    envfactor = forms.IntegerField(label="")
    roofarea = forms.IntegerField(label="")
    
    
    
    #size estimate sama panel ga dimasukin ke forms, soalnya itu output