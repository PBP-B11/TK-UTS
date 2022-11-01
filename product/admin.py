from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Inverter)
admin.site.register(Panel)
admin.site.register(Battery)