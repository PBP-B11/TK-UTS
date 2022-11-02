from unittest.util import _MAX_LENGTH
from django.db import models
from mypanel.models import Customer
from django.contrib.auth.models import User

# Create your models here.
class Calculation(models.Model):
    user   = models.ForeignKey(Customer, on_delete=models.CASCADE)
    electricity  = models.TextField()
    offset    = models.TextField()
    envfactor = models.TextField()
    sizeestimate   = models.TextField()
    roofarea   = models.TextField()
    panel = models.TextField()
    requiredarea = models.TextField(blank=True,null=True)
    is_doable = models.BooleanField(blank=True,null=True)
    date = models.DateField(auto_now = True)