from os import stat
import re
from unittest import result
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from testimoni.forms import TestiForm
from testimoni.models import TestiTemplate
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from mypanel.models import *


def show_testi(request):
    data_testi = TestiTemplate.objects.all()
    context = {
    'list_todos': data_testi,
    }
    return render(request, "testimoni.html", context)

def show_json(request):
    data = TestiTemplate.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = TestiTemplate.objects.filter(pk=id)
    #ika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



@login_required(login_url='/login/')
def create(request):
    form = TestiForm()
    if request.method == 'POST':
        form = TestiForm(request.POST)
        if form.is_valid():
            form_listener = form.save(commit=True)
            form_listener.user = request.user
            form_listener.save()
            messages.info(request,'Data berhasil disimpan!')

            return HttpResponseRedirect(reverse('testimoni:show_testi'))
        else:
            messages.info(request,'Terjadi kesalahan saat menyimpan data!')
    context = {'form': form}
    return render(request, 'create.html',context)



@login_required(login_url='/login/')
@csrf_exempt
def create_testi_ajax(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        cust= Customer.objects.get(user=request.user)
        
        testitemplate = TestiTemplate.objects.create(customer=cust, title=title, description=description, date=datetime.date.today(), reply='-')
        testitemplate.save()

        todo = {"title" : testitemplate.title,"description":testitemplate.description, "date":testitemplate.date, "reply": testitemplate.reply}
        return JsonResponse(todo)

def delete(request, id):
    todo_delete = TestiTemplate.objects.filter(pk=id)
    todo_delete.delete()
    return HttpResponseRedirect(reverse('testimoni:show_testi'))

@login_required(login_url='/login/')
@csrf_exempt
def reply(request, id):
    if request.method == 'POST':
        testimoni = TestiTemplate.objects.filter(pk=id)
        reply_get= TestiTemplate.objects.get(pk=id).reply
        print(reply_get)
        testimoni.update(reply=request.POST.get('reply'))
        TestiTemplate.objects.get(pk=id).save()
        result=TestiTemplate.objects.filter(pk=id)
        data=serializers.serialize('json', result)
        return HttpResponse(data, content_type='application/json')
    else:
        return JsonResponse({'error': "Not an ajax request"}, status=400)
        blog = TestiTemplate.objects.create(
            reply = request.POST.get('reply'),
            
        )
        # print(request.user)
        return JsonResponse({
                'fields':{
                'reply':blog.reply,
            }})






