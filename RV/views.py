from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorator import unauthenticated_user


def dashboard(request):
    return render(request, 'RV/dashboard.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'RV/home.html')


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'RV/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def register_page(request):
    form = CreateUserForm(request.POST)
    context = {'form': form}
    if request.method == 'POST':
        form = CreateUserForm()
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Profile Created for ' + user)
            return redirect('login')

    return render(request, 'RV/register.html', context)
