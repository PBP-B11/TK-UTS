from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', show_product, name='product'),
    path('get_product/', get_product, name="get_product"),
] 