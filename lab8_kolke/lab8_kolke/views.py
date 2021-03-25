
# Create your views here.
from django.shortcuts import render


def fibon(request):
    return render(request, 'lab8_kolke/worker_1.html', {})
def numbers(request):
    return render(request, 'lab8_kolke/worker_2.html', {})
