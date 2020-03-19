from django import forms
from .models import *


class UploadForm(forms.Form):
    frontal = forms.ImageField(required=False)
    lateral = forms.ImageField(required=False)

