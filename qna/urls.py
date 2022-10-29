from django.urls import path
from qna.views import show_question, create_question, update_question


app_name = 'qna'

urlpatterns = [
    path('', show_question, name='show_question'),
    path('create_question/', create_question, name='create_question' ),
    path('update_question/<int:id>', update_question, name='update_question'),

]