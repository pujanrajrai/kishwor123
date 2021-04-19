from django.shortcuts import render
from vehicle.models import Vehicle


# Create your views here.

def search(request):
    vehicle = Vehicle.objects.filter(name=request.GET.get('search'))
    print(vehicle)
    context = {"vehicle": vehicle}
    return render(request, 'home/search.html', context)


def home(request):
    return render(request, 'home/index.html')


def after_login(request):
    return render(request, 'home/afterlogin.html')
