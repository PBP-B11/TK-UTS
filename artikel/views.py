from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.core import serializers
from django.db.models import Count

from artikel.models import Artikel
from artikel.forms import addArticle
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from mypanel.models import Customer



# Create your views here.
# @login_required(login_url='../login/')
def show_article(request):
    if request.user.is_anonymous :
        user = None
    else :
        user = Customer.objects.get(user=request.user)
        # user.is_technician =True

    form = addArticle()
    context = {
    'user': user,
    'form':form
    }
    return render(request, "artikel.html",context)

def artikel_json(request):
    data = Artikel.objects.filter(status = True).order_by('-date')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def artikel_populer_json(request):
    # data = Artikel.objects.annotate(like_count=Count('like')).filter(status = True).order_by('-like_count')[:3]
    data = Artikel.objects.filter(status = True).order_by('-like')[:3]
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def artikel_user_json(request):
    user = Customer.objects.get(user=request.user)
    data = Artikel.objects.filter(user = user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def artikel_submitted_json(request):
    data = Artikel.objects.filter(status = False)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def add_article(request):
    if request.method == 'POST':
        userLogin = Customer.objects.get(user=request.user)
        if userLogin.is_technician :
            status = True
        else :
            status = False

        title  = request.POST.get('title')
        url    = request.POST.get('url')
        gambar = request.POST.get('gambar')
        Artikel.objects.create(
            user   = userLogin,
            title  = title,
            url    = url,
            gambar = gambar,
            status = status,
        )
    return JsonResponse({}, status=200)

def delete_article(request, id):
    if request.method == 'POST':
        artikel = Artikel.objects.get(id=id)
        artikel.delete()
        
    return JsonResponse({}, status=200)


def add_like(request, id):
    if request.method == 'POST':
        artikel = Artikel.objects.get(id=id)
        artikel.like += 1
        artikel.save()
        
    return JsonResponse({}, status=200)

def approve_article(request, id):
    if request.method == 'POST':
        artikel = Artikel.objects.get(id=id)
        artikel.status = True
        artikel.save()
        
    return JsonResponse({}, status=200)


