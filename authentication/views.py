from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from mypanel.models import *
from django.contrib.auth.models import User

@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        register_as = request.POST.get('register_as')

        if password1 != password2:
            return JsonResponse({'status': False, 'message': 'Password tidak sesuai'}, status=400)
        user = User.objects.create_user(username=username, password=password1)
        
        try:
            customer = Customer.objects.get(user=user)
        except:
            customer = Customer.objects.create(
                user=user, 
                name=user.get_username(), 
                email="None", 
                phone="None",
                is_technician=register_as == "Technician"
            )
        return JsonResponse({'status': True}, status=200)

from mypanel.models import Customer


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            customer = Customer.objects.filter(user=user)
            query_cust = customer.values()
            # Redirect to a success page.
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                "user": list(query_cust)[0],
            }, status=200)

        else:
            return JsonResponse({
                "status": False,
                "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
        }, status=401)
