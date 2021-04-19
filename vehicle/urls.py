from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home)
# ]

from django.urls import path
from . import views

app_name = 'vehicle'
urlpatterns = [
    path('add/', views.add_vehicle, name='add_vehicle'),
    path('bike_view/', views.bike_show, name='bike_view'),
    path('car_view/', views.car_show, name='car_view'),
    path('booking/<int:id>', views.vehicle_book, name='vehicle_book'),
    path('vehicle_details/<int:id>/', views.vehicle_details, name='vehicle_details'),
]
