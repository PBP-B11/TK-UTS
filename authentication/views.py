from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.http import JsonResponse

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from mypanel.models import Customer


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.

            customer = Customer.objects.get(user=request.user)

            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!",
            # Insert any extra data if you want to pass data to Flutter
            "is_technician": customer.is_technician,
            }, status=200)



            # return( Customer.objects.get(user=request.user).name)
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
