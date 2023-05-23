from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import User
from django.contrib.auth import logout
from .forms import UserloginForm, UserRegistrationForm, UserProfileForm
from django.contrib import  auth
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        form = UserloginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/users/profile')
    else:
        form = UserloginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def reg(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/log/')
        else:
            print('aaaaaaaaaaaaaaaaaaaa')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def profile(request):
    form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/profile.html', context)

def logoutPage(request):
    logout(request)
    return redirect('/')




