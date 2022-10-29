from django.urls import path
from kalkulator.views import show_calculator
from kalkulator.views import show_json
from kalkulator.views import add_history

app_name = 'kalkulator'

urlpatterns = [
    path('',show_calculator,name='show_calculator'),
]