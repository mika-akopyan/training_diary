from django import forms

from .models import *


class AsanasForm(forms.ModelForm):
    class Meta:
        model = Asanas
        fields = ['sequence_number', 'asana', 'technique_execution', 'works_time', 'sides_quantity']
        