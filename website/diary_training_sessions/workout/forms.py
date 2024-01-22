from django import forms

from .models import *


class ExercisesForm(forms.ModelForm):
    class Meta:
        model = Exercises
        fields = ['muscle', 'exercise', 'technique_execution', 'sides_quantity']
