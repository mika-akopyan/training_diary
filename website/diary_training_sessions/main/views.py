from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .forms import *

# Create your views here.

def index(requst):
    return render(requst, 'main/index.html')


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'main/user_registration.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


class UserAuthenticationView(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'main/user_authentication.html'
    context_object_name = 'form'
