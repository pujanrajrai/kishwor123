from django.contrib import admin
from .models import Vehicle,VehicleType,VehicleBooking

# Register your models here.

admin.site.register(Vehicle)
admin.site.register(VehicleBooking)
admin.site.register(VehicleType)