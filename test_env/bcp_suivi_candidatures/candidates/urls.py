from django.urls import path
from . import views

app_name = 'candidates'

urlpatterns = [
    path('', views.candidates_list, name='list'),
    path('<slug:slug>', views.candidate_details, name='details'),
]
