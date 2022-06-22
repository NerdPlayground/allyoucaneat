from cmath import log
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from custom_user.forms import RegistrationForm,AuthenticationForm

def redirect_user(user):
    if user.customer:
        return HttpResponseRedirect(reverse("products:products"))
    elif user.sasapay_vendor or user.external_vendor:
        return HttpResponseRedirect(reverse("vendors:customer-orders"))
    elif user.is_staff:
        return HttpResponseRedirect(reverse("products:all-products"))

def home(request):
    if request.user.is_authenticated:
        return redirect_user(request.user)
    context= {}
    return render(request,"home.html",context)

def register(request):
    form= RegistrationForm()
    if request.method == 'POST':
        form= RegistrationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            role= form.cleaned_data["role"]

            if role == "Customer":
                user.customer= True
            elif role == "External Vendor":
                user.external_vendor= True
            elif role == "SasaPay Vendor":
                user.sasapay_vendor= True
            else:
                messages.error(request,"Error: Select existing role")
            
            user.username= user.id
            user.save()
            login(request,user)
            return redirect_user(user)
        else:
            messages.error(request,"Error: Unable to register user")
    context= {"form":form}
    return render(request,'custom_user/registration.html',context)

def authenticate_user(request):
    if request.user.is_authenticated:
        return redirect_user(request.user)
    
    form= AuthenticationForm()
    if request.method == "POST":
        form= AuthenticationForm(request.POST)
        if form.is_valid():
            username= request.POST.get("phone_number")
            password= request.POST.get("password")
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect_user(user)
            else:
                messages.error(request,"Error: User with provided credentials does not exist")
        else:
            messages.error(request,"Error: Unable to authenticate user")
    context= {"form":form}
    return render(request,'custom_user/authentication.html',context)

@login_required(login_url="user:login")
def profile(request):
    user= request.user
    if request.method == 'POST':
        edited_first_name= request.POST.get('profile-first-name')
        user.first_name= edited_first_name if edited_first_name is not None else user.first_name

        edited_last_name= request.POST.get('profile-last-name')
        user.last_name= edited_last_name if edited_last_name is not None else user.last_name

        edited_email= request.POST.get('profile-email')
        user.email= edited_email if edited_email is not None else user.email

        edited_phone_number= request.POST.get('profile-phone-number')
        if len(edited_phone_number) == 13:
            user.phone_number= edited_phone_number if edited_phone_number is not None else user.phone_number
            user.save()
            return HttpResponseRedirect(reverse("user:profile"))
        
    context= {"user":user}
    return render(request,"custom_user/profile.html",context)

@login_required(login_url="user:login")
def delete_profile(request):
    user= request.user
    if request.method == "POST":
        user.delete()
        return HttpResponseRedirect(reverse("home"))
    context= {"obj":user}
    return render(request,"delete.html",context)

@login_required(login_url="user:login")
def logout_user(request):
    logout(request)
    return redirect("home")