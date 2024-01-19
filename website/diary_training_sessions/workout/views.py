from django.shortcuts import render

# Create your views here.

def creation(request):
    return render(request, 'workout/creation.html')


def viewing(request):
    return render(request, 'workout/viewing.html')


def exercises(request):
    return render(request, 'workout/exercises.html')
