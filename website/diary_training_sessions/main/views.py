from django.shortcuts import render, HttpResponse

# Create your views here.

def index(requst):
    return render(requst, 'main/index.html')
