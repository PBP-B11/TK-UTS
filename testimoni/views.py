from django.shortcuts import render, get_object_or_404
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
    return HttpResponse(serializers.serialize("json", data, use_natural_foreign_keys=True, use_natural_primary_keys=True), content_type="application/json")

def show_json_by_id(request, id):
    data = TestiTemplate.objects.filter(pk=id)
    #ika JSON
    return HttpResponse(serializers.serialize("json", data,  use_natural_foreign_keys=True, use_natural_primary_keys=True), content_type="application/json")




@login_required(login_url='/login/')
@csrf_exempt
def create_testi_ajax(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        namacust= Customer.objects.get(user=request.user)
        
    
        
        testitemplate = TestiTemplate.objects.create(customer=namacust, title=title, description=description, date=datetime.date.today())
        
        serialize_json = serializers.serialize('json', [testitemplate],use_natural_foreign_keys=True, use_natural_primary_keys=True)
        print(serialize_json)
        return HttpResponse(serialize_json)


@login_required(login_url='/todolist/login')
@csrf_exempt

def delete(request, id):
    if request.method == "DELETE":
        print("passed")
        task = get_object_or_404(TestiTemplate, id = id)
        task.delete()
    return HttpResponse(status=202)

# @login_required(login_url='/login/')
# @csrf_exempt
# def reply(request, id):
#     if request.method == 'POST':
#         testimoni = TestiTemplate.objects.filter(pk=id)
#         reply_get= TestiTemplate.objects.get(pk=id).reply
#         print(reply_get)
#         testimoni.update(reply=request.POST.get('reply'))
#         TestiTemplate.objects.get(pk=id).save()
#         result=TestiTemplate.objects.filter(pk=id)
#         data=serializers.serialize('json', result)
#         return HttpResponse(data, content_type='application/json')
#     else:
#         return JsonResponse({'error': "Not an ajax request"}, status=400)
#         blog = TestiTemplate.objects.create(
#             reply = request.POST.get('reply'),
            
#         )
#         # print(request.user)
#         return JsonResponse({
#                 'fields':{
#                 'reply':blog.reply,
#             }})






