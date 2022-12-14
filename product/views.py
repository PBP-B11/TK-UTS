import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from mycart.models import *
from mypanel.models import *
from .models import *
from .forms import *
from itertools import chain

@login_required(login_url='/login/')
def show_product(request):
    context = {
        'forms': ProductForm(),
        'customer': Customer.objects.get(user=request.user)}
    return render(request, "product.html", context)

@login_required(login_url='/login/')
def get_product(request):
    product_list = Product.objects.all()
    # return HttpResponse(
    #     serializers.serialize(
    #         "json", 
    #         product_list, 
    #         use_natural_foreign_keys=True,
    #         ), 
    #     content_type="application/json",)
    serialized_queryset = serializers.serialize('python', product_list)
    return JsonResponse(serialized_queryset, safe=False, status=200)

@login_required(login_url='/login/')
@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        price = request.POST.get('price')
        image = request.POST.get('image')
        if type == "Panel":
            product = Panel.objects.create(
                name=name+" (Panel)",
                price=price,
                max_power=request.POST.get('max_power'),
                image=image)
        elif type == "Battery":
            product = Battery.objects.create(
                name=name+" (Battery)",
                price=price,
                capacity=request.POST.get('capacity'),
                image=image)
        elif type == "Inverter":
            product = Inverter.objects.create(
                name=name+" (Inverter)",
                price=price,
                output=request.POST.get('output'),
                image=image)

        return HttpResponse(
            serializers.serialize(
                "json", 
                {product.get_parent()}, 
                use_natural_foreign_keys=True,
                ), 
            content_type="application/json",
            status=200)

@login_required(login_url='/login/')
@csrf_exempt
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    customer = Customer.objects.get(user=request.user)
    print(customer.name)
    myorder = Order.objects.get_or_create(customer=customer, is_complete=False, on_process=False)
    try:
        order_item = OrderItem.objects.get(product=product, order=myorder[0].id)
    except OrderItem.DoesNotExist:
        order_item = OrderItem.objects.create(
            product=product,
            order=myorder[0],
            quantity=1,
        )
    else:
        order_item.quantity += 1
        order_item.save()
   
    return JsonResponse({'status':'200'})
    
    # return HttpResponse(
    #         serializers.serialize(
    #             "json", 
    #             order_item, 
    #             use_natural_foreign_keys=True,
    #             ), 
    #         content_type="application/json")