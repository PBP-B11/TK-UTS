from django.db import models
from django.contrib.auth.models import User
from mypanel.models import Customer

class MainAddress(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False, default="")
	kota = models.CharField(max_length=200, null=False, default="")
	kecamatan = models.CharField(max_length=200, null=False, default="")
	kelurahan = models.CharField(max_length=200, null=False, default="")
	postcode = models.CharField(max_length=200, null=False, default="")