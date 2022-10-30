from django import forms

class question_form(forms.Form):
    description = forms.CharField(label="Question", widget=forms.Textarea)