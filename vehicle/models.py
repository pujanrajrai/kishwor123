from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from accounts.models import MyUser


class VehicleType(models.Model):
    type = models.CharField(max_length=100)
    type_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Vehicle(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20)
    vehicle = models.ImageField()
    km_driven = models.PositiveSmallIntegerField()
    seat = models.PositiveSmallIntegerField()
    price_per_day = models.CharField(max_length=100)
    wheeler = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    details = models.CharField(max_length=100)
    is_available = models.CharField(max_length=100, default=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class VehicleBooking(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='owner')
    buyer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='buyer')
    order_date = models.DateField()
    order_expire_date = models.DateField()
    total_price = models.PositiveIntegerField()
