from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.

def creation(request):
    return render(request, 'yoga/creation.html')


def viewing(request):
    return render(request, 'yoga/viewing.html')


class AsanasListView(ListView):
    model = Asanas
    template_name = 'yoga/asanas_list.html'
    context_object_name = 'asanas'
    paginate_by = 7


class AsanaAddView(CreateView):
    form_class = AsanasForm
    template_name = 'yoga/asana_add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('yoga:asanas')


class AsanaDetailView(DetailView):
    model = Asanas
    template_name = 'yoga/asana_detail.html'
    context_object_name = 'asana'
    pk_url_kwarg = 'asana_pk'
