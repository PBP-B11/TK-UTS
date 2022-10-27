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
from mypanel.models import *

@login_required(login_url='/login/')
def cart(request):
    customer = Customer.objects.get(user=request.user)
    mycart = Order.objects.get_or_create(customer=customer, is_complete=False)
    context = {
        'cart': mycart
    }
    return render(request, 'cart.html', context)
    
def get_mycart(request):
    customer = Customer.objects.get(user=request.user)
    myorder = Order.objects.get(customer=customer)
    cart_list = OrderItem.objects.filter(order=myorder)
    print(cart_list)
    return HttpResponse(
        serializers.serialize(
            "json", 
            cart_list, 
            use_natural_foreign_keys=True, 
            use_natural_primary_keys=True), 
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
    return HttpResponseRedirect(reverse('cart:cart'))

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