from curses import panel
import math
from django.shortcuts import render
from kalkulator.models import Calculation
from kalkulator.forms import AddHistory
from mypanel.models import Customer
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers


from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from mypanel.models import Customer
# Create your views here.

def coba(request):
    context={

    }
    return render(request,"coba.html",context)

@login_required(login_url='../login/')
@csrf_exempt
def show_calculator(request):
    form = AddHistory()
    user = Customer.objects.get(user=request.user)
    context = {
        'form':form,
    }
    if request.method == 'POST':
        form = AddHistory(request.POST)
        userLogin = Customer.objects.get(user=request.user)
        if form.is_valid():
            tagihanlistrik = form.cleaned_data['electricity']
            daya = form.cleaned_data['offset']
            faktorlingkungan = form.cleaned_data['envfactor']
            luasatap = form.cleaned_data['roofarea']
            doable = True
            solar_hours = 3.7 #solarhours itu intensitas matahari ke suatu daerah, kalo indo, rata-rata 3.7
            solar_array_output = math.ceil(tagihanlistrik / (365*solar_hours))
            solar_size = math.ceil(solar_array_output * ((daya/100)/(faktorlingkungan/100)))
            required_panel = math.ceil((solar_size * 1000)/(300))
            required_area = math.ceil(required_panel*1.4) #1.4 itu luas tiap panel
            if required_area > luasatap:
                doable = False

            Calculation.objects.create(
                user   = userLogin,
                electricity  = tagihanlistrik,
                offset    = daya ,
                envfactor = faktorlingkungan,
                sizeestimate = solar_size,
                roofarea =luasatap,
                panel = required_panel,
                requiredarea = required_area,
                is_doable = doable,
            )
    return render(request,"kalkulator.html",context)

def show_json(request):
    user = Customer.objects.get(user=request.user)
    data_history = Calculation.objects.filter(user=user)
    return HttpResponse(serializers.serialize('json', data_history), content_type="application/json")

