from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .forms import *

# Create your views here.

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect('home')


class UserAuthenticationView(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'user/user_authentication.html'
    context_object_name = 'form'


def logout_user(request):
    logout(request)
    return redirect('home')
