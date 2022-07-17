import re
from orders.models import Order
from django.urls import reverse
from django.contrib import messages
from vendors.decorators import is_vendor
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from vendors.forms import VendorRegistration,ModificationForm
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect

from vendors.models import Vendor 

def register_vendor(request,role):
    form= VendorRegistration()
    if request.method == "POST":
        form= VendorRegistration(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            if role == "sasapay_vendor":
                user.sasapay_vendor= True
            elif role == "external_vendor":
                user.external_vendor= True
            else:
                messages.error(request,"Error: Unable to register vendor")
            user.username= user.id
            user.save()
            login(request,user)
            return HttpResponseRedirect(reverse("vendors:customer-orders"))
        else:
            messages.error(request,"Error: Unable to register vendor")
    context= {"form":form}
    return render(request,"vendors/registration.html",context)

def register_external_vendor(request):
    return register_vendor(request,role="external_vendor")

def register_sasapay_vendor(request):
    return register_vendor(request,role="sasapay_vendor")

@login_required(login_url="user:login")
def modify_user(request):
    user= Vendor.objects.get(id=request.user.id)
    form= ModificationForm(instance=user)
    data= request.POST
    if request.method == "POST":
        user.first_name= data.get("first_name")
        user.last_name= data.get("last_name")
        user.email= data.get("email")
        user.phone_number= data.get("phone_number")
        user.business_name= data.get("business_name")
        user.till_number= data.get("till_number")
        user.save()
        return HttpResponseRedirect(reverse("user:profile"))
    context= {"form":form,"user":user}
    return render(request,"custom_user/modification.html",context)

@login_required(login_url="user:login")
@is_vendor
def orders(request):
    context= {}
    return render(request,"vendors/orders.html",context)

@login_required(login_url="user:login")
@is_vendor
def receipts(request):
    context= {}
    return render(request,"vendors/receipts.html",context)