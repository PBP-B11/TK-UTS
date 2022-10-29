from django.db import models
from mypanel.models import Customer

# Create your models here.
class TestiTemplate(models.Model):
    id = models.AutoField (primary_key= True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    reply = models.TextField()

