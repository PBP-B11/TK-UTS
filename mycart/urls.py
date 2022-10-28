from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('get_cart', get_mycart, name="get_mycart"),
    path('inc_dec_item/<int:inc_dec>/<int:pk>', inc_dec_item, name="inc_dec_item"),
    path('delete/<int:pk>', delete, name="delete"),
    path('checkout', show_checkout, name="show_checkout")
] 