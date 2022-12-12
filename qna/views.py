from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from mypanel.models import Customer
from qna.models import question
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.core import serializers

@login_required(login_url='/login/')
def show_question(request):
    data_question = question.objects.all()
    user_id = request.COOKIES['user']
    user = Customer.objects.get(user_id = user_id)
    context = {
        'question_list' : data_question,
        'user' : user
    }
    return render(request, "show_qna.html", context)

def show_question_json(request) :
    data_question = question.objects.all()
    data = []
    for item in data_question :
        data.append(
            {"pk": item.pk, 
            "fields": {"customer": item.customer.id, "is_technician": item.customer.is_technician,
            "date": item.date, "description": item.description, 
            "is_replied": item.is_replied, "answer": item.answer}})
    data = {'data' : data}
    return JsonResponse(data)


@login_required(login_url='/login/')
def create_question(request):
    if(request.method == "POST") :
        user_id = request.COOKIES['user']
        customer = Customer.objects.get(pk = user_id)
        question.objects.create(
            customer = customer,
            date = datetime.now(),
            description = request.POST['description']
        )
        return redirect(("qna:show_question"))
    return render(request, "create_question.html")

@login_required(login_url='/login/')
def update_question(request,id):
    if request.method == "POST" :
        object_question = question.objects.filter(pk=id)[0]
        object_question.is_replied = True
        object_question.answer = request.POST['answer']
        object_question.save()
    return HttpResponse({"Message: Succes"})


def show_json(request):
    data_json = question.object.all()
    return HttpResponse(serializers("json", data_json),content_type = "apllication/json")