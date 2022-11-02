from django import forms

class ProductForm(forms.Form):
    CHOICES = [
        ('Panel', 'Panel'),
        ('Battery', 'Battery'),
        ('Inverter', 'Inverter'),
    ]
    name = forms.CharField(label='', max_length=64, widget=forms.TextInput(attrs={'id':'input-name'}))
    type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id':'input-type'}))
    max_power = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'id':'input-maxpower'}))
    capacity = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'id':'input-capacity'}))
    output = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'id':'input-output'}))
    price = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'id':'input-price'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'input-image'}))