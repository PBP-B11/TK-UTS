from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', show_product, name='product'),
    path('get_product/', get_product, name="get_product"),
    path('add_product/', add_product, name="add_product"),
    path('add_to_cart/<int:pk>', add_to_cart, name="add_to_cart"),
] 