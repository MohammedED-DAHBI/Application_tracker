from django.urls import path
from . import views

app_name = 'candidates'

urlpatterns = [
    path('', views.candidates_list, name='list'),
    path('data', views.candidates_json, name='data'),
    path('new', views.new_candidate, name='new'),
    path('<int:id>', views.candidate_details, name='details'),
]