from django import forms
from .models import *


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('frontal', 'lateral', 'prediction', 'explanations',)

