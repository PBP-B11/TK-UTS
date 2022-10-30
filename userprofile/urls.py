from django.urls import path
from userprofile.views import *

app_name = 'userprofile'

urlpatterns = [
    path('', profile, name='profile'),
    path('json1/', show_json_cust, name='show_json1'),
    path('json2/', show_json_addr, name='show_json2'),
    path('change-name/', change_name, name='change_name'),
    path('change-cont/', change_contact, name='change_cont'),
    path('change-addr/', change_address, name='change_addr'),
]