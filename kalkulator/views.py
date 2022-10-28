from django.shortcuts import render
from kalkulator.models import Kalkulator
from kalkulator.forms import addHistory
from mypanel.models import Customer


from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

from django.contrib.auth.models import User
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

# Create your views here.

def show_calculator(request):
    form = addHistory()
    user = request.user
    data_history = Kalkulator.objects.filter(user=user)
    context = {
        'form':form,
        'data_history':data_history,
        'user':user,
    }
    return render(request,"kalkulator.html",context)

def show_json(request):
    user = Customer.objects.get(user=request.user)
    data_history = Kalkulator.objects.filter(user=user)
    return HttpResponse(serializers)

def add_history(request):
    form = addHistory()
    if request.method == 'POST':
        form = addHistory(request.POST)
        if form.is_valid():
            todolist = form.save(commit = False)
            todolist.user = request.user
            form.save()
            return redirect('kalkulator:show_calculator')
