from django.urls import path
from qna.views import *


app_name = 'qna'

urlpatterns = [
    path('', show_question, name='show_question'),
    path('create_question/', create_question, name='create_question' ),
    path('update_question/<int:id>', update_question, name='update_question'),
    path('show_question_json', show_question_json, name = 'show_question_json'),
    path('show_json', show_json, name = 'show_json')
]