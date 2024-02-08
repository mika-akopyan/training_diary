from django import forms

from .models import *


class AsanasForm(forms.ModelForm):
    class Meta:
        model = Asanas
        fields = ['sequence_number', 'asana', 'technique_execution', 'works_time', 'sides_quantity']
        widgets = {
            'sequence_number': forms.NumberInput(attrs={'class': 'form__input'}),
            'asana': forms.TextInput(attrs={'class': 'form__input'}),
            'technique_execution': forms.Textarea(attrs={'class': 'form__input'}),
            'works_time': forms.TextInput(attrs={'class': 'form__input'}),
            'sides_quantity': forms.NumberInput(attrs={'class': 'form__input'})
        }
        