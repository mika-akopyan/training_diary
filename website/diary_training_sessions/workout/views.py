from django.shortcuts import render
from django.views.generic import ListView

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
