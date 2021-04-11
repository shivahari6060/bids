from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def siteHome(request):
    context={}
    return render(request, 'main.html', context)

def Login(request):
    form= AuthenticationForm()
    next= ""
    if request.GET:
        next= request.GET['next']
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next=='':
                return HttpResponseRedirect('/polls/dashboard')
            else:
                return HttpResponseRedirect(next)
        else:
            messages.info(request, 'Username or Password is incorrect !')
    context={
        'form':form,
        'next':next,
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
