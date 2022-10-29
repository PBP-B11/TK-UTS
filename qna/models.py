import imp
from django.db import models
from mypanel.models import Customer

# Create your models here.
class question(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    description = models.TextField()
    is_replied = models.BooleanField(default= False)
