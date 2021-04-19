from django.shortcuts import render, redirect
from vehicle.models import VehicleBooking, Vehicle,VehicleType
from datetime import datetime
from accounts.models import MyUser
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'vehicle/vechile.html', )


from django.shortcuts import render
from .forms import VehicleForms
from .models import Vehicle


# Create your views here.

def add_vehicle(request):
    forms=VehicleForms()
    if request.method == 'POST':

        forms = VehicleForms(request.POST, request.FILES)
        if forms.is_valid():

            vehicle = Vehicle(
                owner=request.user,
                name=request.POST.get('name'),
                km_driven=request.POST.get('km_driven'),
                seat=request.POST.get('seat'),
                price_per_day=request.POST.get('price_per_day'),
                wheeler=request.POST.get('wheeler'),
                transmission=request.POST.get('transmission'),
                type=VehicleType.objects.get(id=request.POST.get('type')),
                details=request.POST.get('details'),
                number_plate=request.POST.get('number_plate'),
                vehicle=request.FILES['vehicle'],
            )

            vehicle.save()
        else:
            print(forms.errors)
            types = VehicleType.objects.all()
            context = {"errors": forms.errors, "types": types}
            return render(request, 'vehicle/addVehicle.html', context)
    types = VehicleType.objects.all()
    context = {"types": types,"forms":forms}
    return redirect('profiles:view')


def bike_show(request):
    vehicles = Vehicle.objects.filter(
        Q(type__type='bike') & Q(is_available=True)
    )
    context = {"vehicles": vehicles}
    return render(request, 'vehicle/vechile.html', context)


def car_show(request):
    vehicles = Vehicle.objects.filter(Q(type__type='car') & Q(is_available=True))
    context = {"vehicles": vehicles}
    return render(request, 'vehicle/vechile.html', context)


@login_required
def vehicle_book(request, id):
    if request.method == 'POST':
        order_date = request.POST.get('order_date')
        order_expire_date = request.POST.get('order_expire_date')
        vehicle = Vehicle.objects.get(id=id)

        booking = VehicleBooking(
            owner=vehicle.owner,
            buyer=request.user,
            order_date=request.POST.get('order_date'),
            order_expire_date=request.POST.get('order_expire_date'),
            total_price=vehicle.price_per_day

        )
        booking.save()
        Vehicle.objects.filter(id=id).update(is_booked=True, is_available=False)
        return redirect('/')


def vehicle_details(request, id):
    vehicle = Vehicle.objects.get(id=id)
    context = {"vehicle": vehicle, "id": id}
    return render(request, 'vehicle/vehicle_details.html', context)
