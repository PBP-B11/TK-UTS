from django.shortcuts import render
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
from .models import Order, OrderItem

@login_required(login_url='/login/')
def cart(request):
    context = {}
    return render(request, 'cart.html', context)
    #return redirect_to_login('mypanel:cart')