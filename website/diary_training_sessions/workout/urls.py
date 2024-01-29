from django.urls import path

from .views import *

app_name = 'workout'
urlpatterns = [
    path('creation/', creation, name='creation'),
    path('viewing/', viewing, name='viewing'),
    path('exercises/', ExercisesListView.as_view(), name='exercises_list'),
    path('exercises/add/', ExerciseAddView.as_view(), name='exercise_add'),
    path('exercises/<str:exercise_pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercises/<str:exercise_pk>/update/', ExerciseUpdateView.as_view(), name='exercise_update'),
]
