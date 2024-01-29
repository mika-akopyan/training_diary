from django.urls import path

from .views import *

app_name = 'yoga'
urlpatterns = [
    path('creation/', creation, name='creation'),
    path('viewing/', viewing, name='viewing'),
    path('asanas/', asanas, name='asanas_list'),
]
