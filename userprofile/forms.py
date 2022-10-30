from django.forms import ModelForm
from mypanel.models import Customer
from userprofile.models import MainAddress

class NameForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('name',)

class ContactForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('email', 'phone')

class AddressForm(ModelForm):
    class Meta:
        model = MainAddress
        fields =('address', 'kota', 'kecamatan', 'kelurahan', 'postcode')