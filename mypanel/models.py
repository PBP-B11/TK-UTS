from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Panel(Product):
    max_power = models.IntegerField()

class Battery(Product):
    capacity = models.IntegerField()

class Inverter(Product):
    output = models.IntegerField()