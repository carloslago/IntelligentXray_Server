from django.shortcuts import render
from .forms import *
from django.template.context_processors import csrf
from .functions import *
import os


def home(request):
    return render(request, "index.html")


def test(request):
    context = {}
    test = Test.objects.all()[0]
    context['pathologies'] = test.prediction
    return render(request, "sample_test.html", context)


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
                images = []
                if frontal is not None and lateral is not None:
                    pathologies = predict_all(request.POST['action'], frontal=test.frontal.path,
                                              lateral=test.lateral.path)
                elif frontal is not None:
                    pathologies = predict_all(request.POST['action'], frontal=test.frontal.path)
                else:
                    pathologies = predict_all(request.POST['action'], lateral=test.lateral.path)
                test.prediction = pathologies
                test.save()
                context['pathologies'] = pathologies
                context['visibility'] = "visible"
                context['test'] = test
    else:
        form = TestForm
        context['visibility'] = "hidden"
    return render(request, "predict.html", context)
