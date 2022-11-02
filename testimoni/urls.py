from ast import Delete
from django.urls import path
from testimoni.views import *




app_name = 'testimoni'

urlpatterns = [
    path('', show_testi, name='show_testi'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('create-ajax/', create_testi_ajax, name= 'create_testi_ajax'),
    path('delete/<int:id>', delete, name='delete'),
]