from django import forms
from .models import Vehicle


class VehicleForms(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'name',
            'km_driven',
            'seat',
            'price_per_day',
            'wheeler',
            'transmission',
            'type',
            'details',
            'number_plate',
            'vehicle',
        ]