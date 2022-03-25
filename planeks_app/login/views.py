from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logins(request):
    """create new user"""
    if request.method == 'POST':
        print('yes')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    """log-in user"""
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main')
    form = CreateUserForm
    data = {'form': form}
    return render(request, 'login/login.html', data)
