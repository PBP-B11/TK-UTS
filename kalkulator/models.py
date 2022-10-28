from unittest.util import _MAX_LENGTH
from django.db import models
from mypanel.models import Customer
from django.contrib.auth.models import User
# Create your models here.
class Kalkulator(models.Model):
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    electricity  = models.IntegerField()
    offset    = models.IntegerField()
    envfactor = models.IntegerField()
    sizeestimate   = models.IntegerField()
    roofarea   = models.IntegerField()
    panel = models.IntegerField()
    date = models.DateField(auto_now = True)