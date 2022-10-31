from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from mypanel.models import *
from product.models import *

@login_required(login_url='/login/')
def show_checkout(request):
    customer = Customer.objects.get(user=request.user)
    mycart = Order.objects.get_or_create(customer=customer, is_complete=False)
    order_item = OrderItem.objects.filter(order=mycart[0].id)

    try:
        myaddress = Address.objects.filter(customer=customer)
    except:
        myaddress = None
    phone_number = customer.phone
    total_price = 0
    for item in order_item:
        total_price += item.get_total
    context = {
        'cart': mycart,
        'address': myaddress,
        'phone': phone_number,
        'total_price': int(total_price)
    }

    response = render(request, 'checkout.html', context)
    # cek cookie udh ada apa blm
    if response.cookies.get('address') is None: 
        # kalo myaddress ada isinya (udh set address)
        if len(myaddress): 
            response.set_cookie('address', myaddress.first().id)
        # klo address msh kosong
        else: 
            response.set_cookie('address', -1)
    return response

@login_required(login_url='/login/')
def cart(request):
    customer = Customer.objects.get(user=request.user)
    mycart = Order.objects.get_or_create(customer=customer, is_complete=False)
    order_item = OrderItem.objects.filter(order=mycart[0].id)

    total_price = 0
    for item in order_item:
        total_price += item.get_total
    context = {
        'cart': mycart,
        'total_price': int(total_price)
    }

    return render(request, 'cart.html', context)

@login_required(login_url='/login/')
def get_mycart(request):
    customer = Customer.objects.get(user=request.user)
    myorder = Order.objects.get(customer=customer)
    cart_list = OrderItem.objects.filter(order=myorder)
    return HttpResponse(
        serializers.serialize(
            "json", 
            cart_list, 
            use_natural_foreign_keys=True, 
            use_natural_primary_keys=True), 
        content_type="application/json")

@login_required(login_url='/login/')
def get_address(request):
    customer = Customer.objects.get(user=request.user)
    myaddress = Address.objects.filter(customer=customer)
    phone_number = customer.phone
    context = {
        'address': myaddress,
        'phone': phone_number,
    }
    return HttpResponse(
        serializers.serialize(
            "json", 
            myaddress, 
            use_natural_foreign_keys=True,
            ), 
        content_type="application/json")

'''
inc_dec status
2 dec
1 inc
'''
@login_required(login_url='/login/')
def inc_dec_item(request, pk, inc_dec):
    order_item = OrderItem.objects.get(pk=pk)
    if inc_dec == 1:
        order_item.quantity += 1
    elif inc_dec == 2:
        if order_item.quantity <= 1:
            pass
        else:
            order_item.quantity -= 1
    order_item.save()
    return HttpResponse(serializers.serialize(
            "json", 
            {order_item},
            use_natural_foreign_keys=True, 
            use_natural_primary_keys=True), 
        content_type="application/json")

@login_required(login_url='/login/')
def delete(request, pk):
    order_item = OrderItem.objects.get(pk=pk)
    order_item.delete()
    return HttpResponseRedirect(reverse('cart:cart'))

# def get_total_price(request):
#     customer = Customer.objects.get(user=request.user)
#     myorder = Order.objects.get(customer=customer)
#     cart_list = OrderItem.objects.filter(order=myorder)
#     total_price = 0
#     for cart in cart_list:
#         total_price += cart.get_total()