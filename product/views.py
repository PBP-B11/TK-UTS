from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mypanel.models import *
from .models import *
from .forms import *
from itertools import chain

def show_product(request):
    context = {'forms': ProductForm()}
    return render(request, "product.html", context)

def get_product(request):
    panel_list = Panel.objects.all()
    battery_list = Battery.objects.all()
    inverter_list = Inverter.objects.all()
    product_list = chain(panel_list, battery_list, inverter_list)
    return HttpResponse(
        PanelSerializer(panel_list, many=True).data
    )
    # return HttpResponse(
    #     serializers.serialize(
    #         "json", 
    #         product_list, 
    #         use_natural_foreign_keys=True,
    #         ), 
    #     content_type="application/json")

@login_required(login_url='/login/')
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        price = request.POST.get('price')
        image = request.POST.get('image')
        if type == "Panel":
            product = Panel.objects.create(
                name=name,
                price=price,
                max_power=request.POST.get('max_power'),
                image=image)
        elif type == "Battery":
            product = Battery.objects.create(
                name=name,
                price=price,
                capacity=request.POST.get('capacity'),
                image=image)
        elif type == "Inverter":
            product = Inverter.objects.create(
                name=name,
                price=price,
                output=request.POST.get('output'),
                image=image)

        return HttpResponse(
            serializers.serialize(
                "json", 
                {product.get_parent()}, 
                use_natural_foreign_keys=True,
                ), 
            content_type="application/json")