from django.urls import path
from . import views

app_name = 'candidates'

urlpatterns = [
    path('', views.candidates_list, name='list'),
    path('new', views.new_candidate, name='new'),
    path('<slug:slug>', views.candidate_details, name='details'),
]
