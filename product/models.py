from django.db import models
from rest_framework import serializers
		
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
		
class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['name', 'price', 'image']

class Panel(Product):
	max_power = models.IntegerField()
	object = ProductManager()

	def get_parent(self):
		return super()
	
	# def natural_key(self):
	# 	return {'name': self.name, 
	# 		'price': self.price,
	# 		'imageURL': self.imageURL,
	# 		}

class PanelSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=True, read_only=True)

	class Meta:
		model = Panel
		fields = ['product', 'max_power']

class Battery(Product):
	capacity = models.IntegerField()
	object = ProductManager()

	def get_parent(self):
		return super()

	def natural_key(self):
		return {'name': self.name, 
			'price': self.price,
			'imageURL': self.imageURL,
			}

class BatterySerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=True, read_only=True)

	class Meta:
		model = Battery
		fields = ['product', 'capacity']

class Inverter(Product):
	output = models.IntegerField()
	object = ProductManager()

	def get_parent(self):
		return super()

	def natural_key(self):
		return {'name': self.name, 
			'price': self.price,
			'imageURL': self.imageURL,
			}

class InverterSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=True, read_only=True)

	class Meta:
		model = Inverter
		fields = ['product', 'output']

