from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(Request):
    if Request.method == 'POST':
        fm = StudentRegistration(Request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(Request,'addstudent.html',{'form':fm,'stud':stud})


def update_data(Request,id):
    pi = User.objects.get(pk=id)
    if Request.method == 'POST':
        fm = StudentRegistration(Request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    fm = StudentRegistration(instance=pi)
    return render(Request,'updatestudent.html',{'form':fm})

def delete_data(Request,id):
    if Request.method == 'POST':
        pi= User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')