from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from mypanel.models import *
from .models import *

def show_product(request):
    return render(request, "product.html")

def get_product(request):
    product_list = Product.objects.all()
    return HttpResponse(
        serializers.serialize(
            "json", 
            product_list, 
            use_natural_foreign_keys=True,
            ), 
        content_type="application/json")