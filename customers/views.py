from datetime import datetime
from django.urls import reverse
from orders.models import Order
from receipts.models import Receipt
from products.models import Content
from django.contrib import messages
from customers.models import Customers
from common.functions import sort_content
from customers.decorators import is_customer
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from customers.forms import CustomerRegistration,ModificationForm
from django.http import Http404,HttpResponse,HttpResponseRedirect

def errors(form_errors):
    labels= {
        'first_name':"First Name",
        'last_name':"Last Name",
        'phone_number' : "Phone Number",
        'password2':"Password",
    }
    
    formatted_output= str()
    for label in form_errors:
        formatted_output += (labels[label] + ": ")
        label_errors= form_errors[label]
        for label_error in label_errors:
            formatted_output += ("".join(label_error))
        formatted_output += "\n\n"
    
    return formatted_output

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
            messages.error(
                request,
                "Registration: Unable to register Customer.\n"
                +"Check if correct data has been provided in the available fields."
            )
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
    context= sort_content(request,customer,Receipt)
    context["current_day"]=str(datetime.today().day)
    return render(request,"receipts/receipts.html",context)

@login_required(login_url="user:login")
@is_customer
def track_orders(request):
    customer= Customers.objects.get(id=request.user.id)
    orders= Order.objects.filter(
        customer=customer,delivered=False
    )
    all_orders= dict()
    for order in orders:
        contents= Content.objects.filter(orders=order)
        all_orders[order]= contents
    context= {"all_orders":all_orders}
    return render(request,"orders/undelivered_orders.html",context)