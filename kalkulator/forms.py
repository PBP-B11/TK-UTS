from django import forms
from kalkulator.models import Calculation
class AddHistory(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = {'electricity','offset','envfactor','roofarea'}  
         #size estimate sama panel ga dimasukin ke forms, soalnya itu output