from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('create/', views.create, name='create'),
    path('view/',views.view, name='view')
]
