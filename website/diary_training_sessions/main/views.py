from django.shortcuts import render, HttpResponse

# Create your views here.

def index(requst):
    return HttpResponse('Главная страница')
