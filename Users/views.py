from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import UserLoginForm
from django.contrib import messages
from Users.decorators import unauthenticated_user


@unauthenticated_user
def log_in(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, template_name='loginhome.html')


def log_out(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, template_name='home.html')





