from django.urls import path

from .views import *

urlpatterns = [
    path('creation/', creation, name='workout_creation'),
    path('viewing/', viewing, name='workout_viewing'),
    path('exercises/', ExercisesView.as_view(), name='exercises'),
]