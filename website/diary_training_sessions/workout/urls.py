from django.urls import path

from .views import *

urlpatterns = [
    path('creation/', creation, name='workout_creation'),
    path('viewing/', viewing, name='workout_viewing'),
    path('exercises/', ExercisesList.as_view(), name='exercises_list'),
    path('exercises/add/', ExerciseAdd.as_view(), name='exercise_add'),
    path('exercises/<str:exercise_pk>/', ExerciseDetail.as_view(), name='exercise_detail'),
]
