from django.urls import path
from .views import *

app_name = 'authentication'

urlpatterns = [
    # path('', homepage, name='homepage'),
    # path('register/', register, name='register'),
    path('login', login, name='login'),
    # path('logout/', logout_user, name='logout'),
]