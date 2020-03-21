from django.shortcuts import render
from .forms import *
from django.template.context_processors import csrf
from .functions import *
import os

def home(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")


def predict(request):
    context = {}
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            frontal = cd.get('frontal')
            lateral = cd.get('lateral')
            if frontal is not None or lateral is not None:
                test = form.save()
                pathologies = predict_img(test.frontal.path)
                test.prediction = pathologies
                test.save()
                print(pathologies)
                context['pathologies'] = pathologies
                context['visibility'] = "visible"
                context['test'] = test
    else:
        form = TestForm
        context['visibility'] = "hidden"
    # token = {}
    # token.update(csrf(request))
    # token['form'] = form
    return render(request, "predict.html", context)
