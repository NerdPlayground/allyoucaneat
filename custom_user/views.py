from cmath import log
from django.urls import reverse
from django.contrib import messages
from django.http import Http404,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from custom_user.forms import RegistrationForm,AuthenticationForm

def register(request):
    form= RegistrationForm()
    if request.method == 'POST':
        form= RegistrationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            status= form.cleaned_data["status"]
            if status == "Customer":
                user.customer= True
                user.save()
                return redirect("")
            elif status == "External Vendor":
                user.external_vendor= True
                user.save()
                return redirect("")
            elif status == "SasaPay Vendor":
                user.saspay_vendor= True
                user.save()
                return redirect("")
            else:
                messages.error("Error: Select existing status")
        else:
            messages.error("Error: Unable to register")
    context= {"form":form}
    return render(request,'custom_user/registration.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect("")
    
    form= AuthenticationForm()
    if request.method == "POST":
        form= AuthenticationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password"]
            user= authenticate(username=username,password=password)
            if user is not None:
                login(user)
                return redirect("")
            else:
                messages.error("Error: User with provided credentials does not exist")
        else:
            messages.error("Error: Unable to authenticate user")
    context= {"form":form}
    return render(request,'custom_user/authentication.html',context)

@login_required(login_url="custom_user:login")
def profile(request):
    context= {}
    return render(request,"custom_user/profile.html",context)

@login_required(login_url="custom_user:login")
def edit_profile(request):
    context= {}
    return render(request,"custom_user/edit_profile.html",context)

@login_required(login_url="custom_user:login")
def delete_profile(request):
    context= {}
    return render(request,"delete.html",context)

@login_required(login_url="custom_user:login")
def logout(request):
    logout(request)
    return redirect("")