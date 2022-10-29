from django.shortcuts import render
from qna.models import question
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse,HttpRequest
from django.core import serializers
from qna.forms import question_form


#@login_required(login_url='login/')
def show_question(request):
    data_question = question.objects.filter(user=request.user).all()
    context = {
        'question_list' : data_question,
    }
    return render(request, "show_qna.html",context)

#@login_required(login_url='/login/')
def create_question(request):
    if request.method == "POST":
        form = question_form(request.POST)
        if form.is_valid():
            new_question = create_question (
                user = request.user,
                description = form.cleaned_data["description"],
                date = datetime.date.today()
            )
            new_question.save()
            return redirect("show_qna:show_question")
    
    form =question_form()
    context = {"form" : form}
    return render(request, "create_question.html", context)
    
#@login_required(login_url='/login/')
def update_question(request,id):
    question = question.objects.filter(pk=id)[0]
    if question.is_replied == True :
        question.is_replied = False
        question.save()
    else:
        question.is_replied = True
        question.save()
    return redirect("show_qna:show_question")