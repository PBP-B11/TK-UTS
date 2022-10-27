from django.db import models
from django.contrib.auth.models import User
from mypanel.models import Customer

# Create your models here.
class Artikel(models.Model):

    # user   = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='poster',null=True)

    user   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster',null=True)
    title  = models.CharField(max_length=100)
    url    = models.URLField()
    gambar = models.URLField()
    like   = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now = True)

