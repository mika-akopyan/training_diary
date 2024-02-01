from django.urls import path

from .views import *

app_name = 'yoga'
urlpatterns = [
    path('creation/', creation, name='creation'),
    path('viewing/', viewing, name='viewing'),
    path('asanas/', AsanasListView.as_view(), name='asanas_list'),
    path('exercises/add/', AsanaAddView.as_view(), name='asana_add'),
    path('asanas/<str:asana_pk>/', AsanaDetailView.as_view(), name='asana_detail'),
    path('asanas/<str:asana_pk>/update/', AsanaUpdateView.as_view(), name='asana_update'),
]
