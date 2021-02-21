from django.shortcuts import render, redirect
from .forms import StudentsForm
# Create your views here.
from django.views.generic import UpdateView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from register.forms import StudentForm, SForm
from register.models import Student, Employee
from register.serializer import EmpSer


def home(request):
    return render(request ,'register/index.html')

def stud_register(request):
    title = 'Student Registration'
    form = StudentForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        addr = form.cleaned_data['saddr']
        dep = form.cleaned_data['sdep']
        sch = form.cleaned_data['ssch']
        res = Student.objects.filter(sname=name)
        if len(res)>0:
            return render(request, 'register/ack.html', {'title': 'Student details already exists'})
        else:
            p = Student(sname=name,saddr=addr,sdep=dep,ssch=sch)
            p.save()
            return render(request,'register/ack.html',{'title':'Registered Successfully'})
    my_dict = {
        'title':title,
        'form':form
    }
    return render(request,'register/stud_reg.html',context=my_dict)

def stud_update(request,pk):
    title = 'Student Update'
    form = StudentForm(request.POST)

    my_dict = {
        'title': title,
        'form': form
    }
    return render(request, 'register/stud_reg.html', context=my_dict)


def stud_delete(request):
    title='Student Delete'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        list = Student.objects.filter(sname=name)
        if len(list)==0:
            return render(request,'register/ack.html',{'title':'Student details not found please enter correct details'})
        else:
            list= Student.objects.filter(sname=name).delete()
            return render(request,'register/ack.html',{'title':'Student deleted successfully'})
    context ={
        'title':title,
        'form':form
    }
    return render(request,'register/delete.html',context)


def stud_all(request):
    title ='Registered Students'
    list = Student.objects.all()
    context = {
        'title':title,
        'list':list
    }
    return render(request,'register/stud_list.html',context)


# class EmpView(APIView):
#     def get(self,request):
#         emps = Employee.objects.all()
#         serializer = EmpSer(emps,many=True)
#         return Response(serializer.data)


def stud_search(request):
    title = 'Search Student'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        list=Student.objects.filter(sname=name)
        if len(list)==0:
            return render(request,'register/ack.html',{'title':'Student details not found try another'})
        my_dict={
            'title':title,
            'list':list
        }
        return render(request,'register/stud_list.html',my_dict)
    my_dict = {
        'title': title,
        'form': form
    }
    return render(request,'register/search.html',my_dict)

class StudentUpdateView(UpdateView):
    model = Student


    fields = [
        "sname","saddr","sdep","ssch"
    ]
    success_url = "/stud-all"

def stud_detailView(request,id):
    context ={

    }
    context["list"]=Student.objects.get(id=id)
    return render(request,'register/stud_detail.html',context)

