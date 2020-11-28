from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url='login')
def dashboard(Request):
    context= {"user":Request.user}
    return render(Request,'dashboard.html',context)


def login_page(Request):
    #context = {'form':form}
    '''if Request.user.is_authenticated:
        return redirect('dashboard')
    else:'''
    if Request.method == 'POST':
        username = Request.POST.get('username')
        password = Request.POST.get('password')

        user = authenticate(Request,username = username,password = password)
        if user is not None:
            login(Request,user)
            return redirect('dashboard')
        else:
            messages.info(Request,'Username or password is incorrect')

    return render(Request,'login.html')
    

def register_page(Request):
    form = CreateUserForm()

    if Request.method == 'POST':
        form = CreateUserForm(Request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(Request, 'Account was created for'+user)
            return redirect('login')
            

    context = {'form':form}
    return render(Request,'register.html',context)

def add_show(Request):
    if Request.method == 'POST':
        fm = StudentRegistration(Request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User1(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User1.objects.all()
    return render(Request,'addstudent.html',{'form':fm,'stud':stud})


def update_data(Request,id):
    pi = User1.objects.get(pk=id)
    if Request.method == 'POST':
        fm = StudentRegistration(Request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    fm = StudentRegistration(instance=pi)
    return render(Request,'updatestudent.html',{'form':fm})

def delete_data(Request,id):
    if Request.method == 'POST':
        pi= User1.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/addshow')


def logoutUser(Request):
    logout(Request)
    return redirect('login')


def static_page(Request):
    return HttpResponse("Hey this is static_page")


def change_password(Request):
    if Request.method == 'POST':
        form = PasswordChangeForm(data=Request.POST,user=Request.user)

        if form.is_valid():
            form.save()
            #update_session_auth_hash(Request,form.user)
            return redirect('dashboard')
        else:
            messages.info(Request,'Password is incorrect')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=Request.user)
        context = {'form':form}
        return render(Request,'changepassword.html',context)