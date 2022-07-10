from django.urls import reverse
from orders.models import Order
from django.contrib import messages
from customers.decorators import is_customer
from django.http import Http404,HttpResponse
from customers.forms import CustomerRegistration
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404

def register_customer(request):
    form= CustomerRegistration()
    if request.method == "POST":
        pass
    context= {"form":form}
    return render(request,"customers/registration.html",context)

@login_required(login_url="user:login")
@is_customer
def orders(request):
    context= {}
    return render(request,"customers/orders.html",context)

@login_required(login_url="user:login")
@is_customer
def track_orders(request):
    context= {}
    return render(request,"customers/track_orders.html",context)