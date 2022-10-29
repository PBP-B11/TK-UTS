from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):	
	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs.update({
            'class' : 'form-control',
        })
		self.fields['password1'].widget.attrs.update({
            'class' : 'form-control',
        })
		self.fields['password2'].widget.attrs.update({
            'class' : 'form-control',
        })