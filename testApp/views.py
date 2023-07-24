from django.shortcuts import render
from django.http import HttpResponse
from testApp.models import Employee
import datetime
from . import forms
# Create your views here.

# Create your views here.
def display(request):
    msg="<h1> Welcome to Django Coding </h1>"
    return HttpResponse(msg)

def wish(request):
    date=datetime.datetime.now()
    msg="All is Well"
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'testApp/wish.html',context=my_dict)

def empdata(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testApp/emp.html',context=my_dict)

def studentinputview(request):
    form=forms.StudentForm()
    my_dict={'form':forms}
    return render(request,'testApp/input.html',context=my_dict)