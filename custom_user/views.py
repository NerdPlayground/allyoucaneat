from django.urls import reverse
from vendors.models import Vendor
from django.contrib import messages
from customers.models import Customers
from custom_user.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect

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

def roles(request):
    url_map={
        "sasapay-vendor": "vendors",
        "external-vendor": "vendors",
        "customer": "customers"
    }

    if request.method == 'POST':
        user_role= request.POST.get("user-roles")
        if user_role != None:
            return HttpResponseRedirect(
                reverse(
                    "%s:register-%s"
                    %(url_map[user_role],user_role)
                )
            )
        else:
            messages.error(request,"Error: Select existing role")
    context= {}
    return render(request,"custom_user/roles.html",context)

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
    customer= user.customer
    vendor= user.sasapay_vendor or user.external_vendor
    user= (
        Customers.objects.get(id=user.id) if customer else
        Vendor.objects.get(id=user.id) if vendor else None
    )

    context= {
        "username":user.username,
        "first_name":user.first_name,
        "last_name":user.last_name,
        "email":user.email,
        "phone_number":user.phone_number,
        "vendor": False
    }
    if vendor:
        context["vendor"]= True
        context["business_name"]= user.business_name
        context["till_number"]= user.till_number
    
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