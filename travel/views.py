from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'travel/base.html');

def annapurna(request):
    return render(request, 'travel/annapurna.html');

