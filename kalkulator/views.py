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

def show_calculator(request):
    form = AddHistory()
    user = Customer.objects.get(user=request.user)
    context = {
        'form':form,
    }
    if request.method == 'POST':
        form = AddHistory(request.POST,instance=user)
        if form.is_valid():
            calculator = form.save(commit = False)
            calculator.user = request.user
            form.save()
            return redirect('kalkulator:show_json')
        
    return render(request,"kalkulator.html",context)

def show_json(request):
    user = Customer.objects.get(user=request.user)
    data_history = Calculation.objects.filter(user=user)
    return HttpResponse(serializers.serialize('json', data_history), content_type="application/json")

@csrf_exempt
def add_history(request):
    print("mantap")
    if request.method == 'POST':
        userLogin = Customer.objects.get(user=request.user)
        tagihanlistrik  = request.POST.get('tagihanlistrik')
        daya    = request.POST.get('daya')
        faktorlingkungan = request.POST.get('faktorlingkungan')
        solar_size = request.POST.get('solar_size')
        luasatap = request.POST.get('luasatap')
        requred_panel = request.POST.get('required_panel')
        required_area = request.POST.get('required_area')


        Calculation.objects.create(
            user   = userLogin,
            electricity  = tagihanlistrik,
            offset    = daya,
            envfactor = faktorlingkungan,
            sizeestimate = solar_size,
            roofarea =luasatap,
            panel = requred_panel,
            requiredarea = required_area
        )
    return JsonResponse({}, status=200)