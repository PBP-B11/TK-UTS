from django.urls import path
from artikel.views import artikel_json, artikel_populer_json, artikel_user_json, artikel_submitted_json
from artikel.views import show_article, add_article, add_like, delete_article, approve_article



app_name = 'artikel'

urlpatterns = [
    path('', show_article, name='show_article'),
    path('artikel-json/', artikel_json, name='artikel_json'),
    path('artikel-populer-json/', artikel_populer_json, name='artikel_populer_json'),
    path('artikel-populer-json/', artikel_populer_json, name='artikel_populer_json'),
    path('artikel-user-json/', artikel_user_json, name='artikel_user_json'),
    path('artikel-submitted-json/', artikel_submitted_json, name='artikel_submitted_json'),
    path('add-article/', add_article, name='add_article' ),
    path('add-like/<int:id>', add_like, name='add_like'),
    path('delete-article/<int:id>', delete_article, name='delete_article'),
    path('approve-article/<int:id>', approve_article, name='approve_article'),

]