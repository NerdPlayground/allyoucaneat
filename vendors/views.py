from orders.models import Order
from django.urls import reverse
from django.contrib import messages
from vendors.decorators import is_vendor
from django.http import Http404,HttpResponse
from vendors.forms import VendorRegistration
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404

def register_vendor(request,role):
    form= VendorRegistration()
    if request.method == "POST":
        pass
    context= {"form":form}
    return render(request,"vendors/registration.html",context)

def register_external_vendor(request):
    return register_vendor(request,role="external_vendor")

def register_sasapay_vendor(request):
    return register_vendor(request,role="sasapay_vendor")


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