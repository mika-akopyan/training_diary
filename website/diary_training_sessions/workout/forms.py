from django import forms

from .models import *


class ExercisesForm(forms.ModelForm):
    class Meta:
        model = Exercises
        fields = ['muscle', 'exercise', 'technique_execution', 'sides_quantity']
        widgets = {
            'muscle': forms.Select(attrs={'class': 'form__input'}),
            'exercise': forms.TextInput(attrs={'class': 'form__input'}),
            'technique_execution': forms.Textarea(attrs={'class': 'form__input'}),
            'sides_quantity': forms.NumberInput(attrs={'class': 'form__input'})
        }
