from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.

def creation(request):
    return render(request, 'workout/creation.html')


def viewing(request):
    return render(request, 'workout/viewing.html')


class ExercisesView(ListView):
    model = Exercises
    template_name = 'workout/exercises.html'
    context_object_name = 'exercises'
    paginate_by = 7


class ExerciseDetail(DetailView):
    model = Exercises
    template_name = 'workout/exercise_detail.html'
    context_object_name = 'exercise'
    pk_url_kwarg = 'exercise_pk'
