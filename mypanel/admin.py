from django.contrib import admin
from mypanel.models import *
from mycart.models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Inverter)
admin.site.register(Panel)
admin.site.register(Battery)