from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import MyUser

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:homepage')
    if request.method == 'POST':
        data = request.POST.copy()
        forms = RegisterForm(data)
        if forms.is_valid():
            user = MyUser(
                email=data['email'],
                password=make_password(data['password']),
                username=data['username'],
                date_of_birth=data['date_of_birth'],
            )
            user.save()
            user = auth.authenticate(email=data['email'], password=data['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            return render(request, 'accounts/register.html')
        else:
            print(forms.errors)
            context = {
                "error": forms.errors,
                "email": data['email'],
                "username": data['username'],
                "date_of_birth": data['date_of_birth']
            }
            return render(request, 'accounts/register.html', context)

    return render(request, 'accounts/register.html')


def login(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('accounts:homepage')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                context = {"errors" : "User name or password is incorrect"}
                return render(request, 'accounts/login.html', context)
        return render(request, 'accounts/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required
def homepage(request):
    return render(request, 'accounts/test.html')