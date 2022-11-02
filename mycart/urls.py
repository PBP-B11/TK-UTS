from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('get_cart/', get_mycart, name="get_mycart"),
    path('inc_dec_item/<int:inc_dec>/<int:pk>/', inc_dec_item, name="inc_dec_item"),
    path('delete/<int:pk>/', delete, name="delete"),
    path('checkout/', show_checkout, name="show_checkout"),
    path('get_address/', get_address, name='get_address'),
    path('process_order/<int:pk>', process_order, name='process_order'),
    path('get_order/', show_order, name='get_order'),
    path('get_order_on_process/', get_order_on_process, name='get_order_on_process'),
    path('finish_order/<int:pk>', finish_order, name='finish_order'),
] 