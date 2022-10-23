import datetime
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from mypanel.models import *

def homepage(request):
    products = Product.objects.all()
    context = {
        'product': products 
    }
    return render(request, 'homepage.html', context)

@login_required(login_url='/login/')
def cart(request):
    context = {}
    return render(request, 'cart.html', context)
    #return redirect_to_login('mypanel:cart')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('mypanel:homepage')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    next_value = request.GET.get('next')
    print(next_value)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            if next_value:
                response = HttpResponseRedirect(next_value) # membuat response
            else:
                response = HttpResponseRedirect(reverse('mypanel:homepage')) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('mypanel:homepage'))
    response.delete_cookie('last_login')
    return response