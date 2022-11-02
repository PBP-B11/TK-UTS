from django.forms import ModelForm
from testimoni.models import TestiTemplate

class TestiForm(ModelForm):
    class Meta:
        model = TestiTemplate
        fields = ['title', 'description', 'reply']