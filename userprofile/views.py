import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from mypanel.models import *
from userprofile.models import MainAddress
from userprofile.forms import *

# Create your views here.
@login_required(login_url='/login/')
def profile(request):
    customers = Customer.objects.get(user=request.user)
    try:
    	address = MainAddress.objects.get(user=request.user) 
    except:
    	address = MainAddress.objects.create(user=request.user, address="None", kota="None", kecamatan="None", kelurahan="None", postcode="")
    context = {'customers': customers, 'address': address}
    return render(request, 'profile.html', context)

@login_required(login_url='/login/')
def change_name(request):
    if request.method == 'POST':
        instance = Customer.objects.get(user=request.user)
        form = NameForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse(b"CREATED", status=201)
    else:
        form = NameForm(request.POST)
    return HttpResponseNotFound()

@login_required(login_url='/login/')
def change_contact(request):
    if request.method == 'POST':
        instance = Customer.objects.get(user=request.user)
        form = ContactForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse(b"CREATED", status=201)
    else:
        form = ContactForm(request.POST)
    return HttpResponseNotFound()

@login_required(login_url='/login/')
def change_address(request):
    if request.method == 'POST':
        instance = MainAddress.objects.get(user=request.user)
        form = AddressForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse(b"CREATED", status=201)
    else:
        form = AddressForm(request.POST)
    return HttpResponseNotFound()

@login_required(login_url='/login/')
def show_json_cust(request):
    data = Customer.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
def show_json_addr(request):
    data = MainAddress.objects.filter(user=request.user) 
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")