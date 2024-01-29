from django.shortcuts import render

# Create your views here.

def creation(request):
    return render(request, 'yoga/creation.html')


def viewing(request):
    return render(request, 'yoga/viewing.html')


def asanas(request):
    return render(request, 'yoga/asanas_list.html')
