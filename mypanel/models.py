from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=255, null=True)
	email = models.CharField(max_length=255, null=True)
	is_technician = models.BooleanField(default=False)
	phone = models.CharField(max_length=20, null=True)
	
	def __str__(self):
		return self.name

class Address(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	kota = models.CharField(max_length=200, null=False)
	kecamatan = models.CharField(max_length=200, null=False)
	kelurahan = models.CharField(max_length=200, null=False)
	postcode = models.CharField(max_length=200, null=False)

	def __str__(self):
		return self.address
		
class ProductManager(models.Manager):
	def get_by_natural_key(self, name, price, imageURL):
		return self.get(name=name, price=price, imageURL=imageURL)

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	image = models.ImageField(upload_to='upload/', null=True, blank=True)

	objects = ProductManager()

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	def natural_key(self):
		return {'name': self.name, 
			'price': self.price,
			'imageURL': self.imageURL,
		}

class Panel(Product):
    max_power = models.IntegerField()

class Battery(Product):
    capacity = models.IntegerField()

class Inverter(Product):
    output = models.IntegerField()