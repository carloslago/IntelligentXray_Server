from django.shortcuts import render
from .forms import *
from django.template.context_processors import csrf

# Create your views here.


def home(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")


def predict(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            frontal = cd.get('frontal')
            lateral = cd.get('lateral')
    else:
        form = UploadForm
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render(request, "predict.html", token)
