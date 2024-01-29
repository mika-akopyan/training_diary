from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.

def creation(request):
    return render(request, 'workout/creation.html')


def viewing(request):
    return render(request, 'workout/viewing.html')


class ExercisesListView(ListView):
    model = Exercises
    template_name = 'workout/exercises_list.html'
    context_object_name = 'exercises'
    paginate_by = 7


class ExerciseAddView(CreateView):
    form_class = ExercisesForm
    template_name = 'workout/exercise_add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('workout:exercises_list')


class ExerciseDetailView(DetailView):
    model = Exercises
    template_name = 'workout/exercise_detail.html'
    context_object_name = 'exercise'
    pk_url_kwarg = 'exercise_pk'


class ExerciseUpdateView(UpdateView):
    form_class = ExercisesForm
    model = Exercises
    template_name = 'workout/exercise_update.html'
    context_object_name = 'form'
    pk_url_kwarg = 'exercise_pk'
    success_url = reverse_lazy('workout:exercises_list')
