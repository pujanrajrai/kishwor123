from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='travel'),
    path('annapurna/', views.annapurna, name='annapurna')

]