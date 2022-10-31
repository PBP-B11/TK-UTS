from django.urls import path
from kalkulator.views import *

app_name = 'kalkulator'

urlpatterns = [
    path('',show_calculator,name='show_calculator'),
    path('show_json',show_json,name='show_json'),
    path('create-ajax',add_history,name="create-ajax"),
]