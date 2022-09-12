from django.urls import reverse
from orders.models import Order
from receipts.models import Receipt
from products.models import Content
from django.contrib import messages
from customers.models import Customers
from customers.decorators import is_customer
from receipts.functions import common_receipts
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from customers.forms import CustomerRegistration,ModificationForm
from django.http import Http404,HttpResponse,HttpResponseRedirect

def register_customer(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("products:products"))

    form= CustomerRegistration()
    if request.method == "POST":
        form= CustomerRegistration(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.customer= True
            user.username= user.id
            user.save()
            login(request,user)
            return HttpResponseRedirect(reverse("products:products"))
        else:
            messages.error(request,"Error: Unable to register customer")
    context= {"form":form}
    return render(request,"customers/registration.html",context)

@login_required(login_url="user:login")
def modify_user(request):
    user= Customers.objects.get(id=request.user.id)
    form= ModificationForm(instance=user)
    data= request.POST
    if request.method == "POST":
        user.first_name= data.get("first_name")
        user.last_name= data.get("last_name")
        user.email= data.get("email")
        user.phone_number= data.get("phone_number")
        user.save()
        return HttpResponseRedirect(reverse("user:profile"))
    context= {"form":form,"user":user}
    return render(request,"custom_user/modification.html",context)

@login_required(login_url="user:login")
@is_customer
def receipts(request):
    customer= Customers.objects.get(id=request.user.id)
    return common_receipts(request,customer)

@login_required(login_url="user:login")
@is_customer
def track_orders(request):
    customer= Customers.objects.get(id=request.user.id)
    orders= Order.objects.filter(
        customer=customer,
        paid=True,delivered=False
    )
    all_orders= dict()
    for order in orders:
        contents= Content.objects.filter(orders=order)
        all_orders[order]= contents
    context= {"all_orders":all_orders}
    return render(request,"orders/undelivered_orders.html",context)