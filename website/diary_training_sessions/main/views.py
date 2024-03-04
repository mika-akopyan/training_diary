from django.shortcuts import render

# Create your views here.

def index(requst):
    return render(requst, 'main/index.html')
