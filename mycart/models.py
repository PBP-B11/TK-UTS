from django.db import models
from mypanel.models import Customer, Product
import json

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	is_complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

	def get_json(self):
		json_data = {
			'product': {
				'name': self.product.name,
				'price': self.product.price,
				'image': self.product.imageURL
			},
			'quantity': self.quantity,
			'date_added': self.date_added.isoformat(),
		}
		return json.dumps(json_data)