from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    context ={}
    return render(request, 'accounts/base.html', context)


def Login(request):
    form= AuthenticationForm()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:index')
        else:
            messages.info(request, 'Username or Password is incorrect !')
    context={
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


def Signup(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        user = request.POST.get('username')
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for '+ user)
            return redirect('accounts:login')

    context={
        'form':form,
    }
    return render(request, 'accounts/register.html', context)


def Logout(request):
    logout(request)
    return redirect('accounts:login')
