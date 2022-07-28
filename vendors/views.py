from orders.models import Order
from django.urls import reverse
from vendors.models import Vendor
from receipts.models import Receipt
from products.models import Content
from django.contrib import messages
from customers.models import Customers
from vendors.decorators import is_vendor
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from vendors.forms import VendorRegistration,ModificationForm
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect

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
            return HttpResponseRedirect(reverse("products:my-shop"))
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
    orders= Order.objects.filter(paid=True,delivered=False)
    all_orders= dict()
    for order in orders:
        contents= Content.objects.filter(orders=order)
        all_orders[order]= contents
    context= {"all_orders":all_orders}
    return render(request,"vendors/orders.html",context)

@login_required(login_url="user:login")
@is_vendor
def deliver_order(request,pk):
    order= Order.objects.get(id=pk)
    order.delivered= True
    order.save()
    
    vendor= Vendor.objects.get(id=request.user.id)
    customer= Customers.objects.get(id=order.customer.id)
    raw_contents= Content.objects.filter(orders=order).values("name")
    contents= list()
    for content in raw_contents:
        contents.append(content.get("name"))

    receipt= Receipt.objects.create(
        product_name=order.product.name,
        contents=contents,
        product_type=order.price.type,
        price=order.price.value,
        customer=customer,
        vendor=vendor,
        shop=vendor.business_name
    )
    receipt.save()
    order.delete()

    undelivered_orders= len(
        Order.objects.filter(paid=True,delivered=False))
    if undelivered_orders == 0:
        return redirect(reverse("products:my-shop"))
    elif undelivered_orders > 0:
        return redirect(reverse("vendors:customers-orders"))

@login_required(login_url="user:login")
@is_vendor
def receipts(request):
    vendor= Vendor.objects.get(id=request.user.id)
    receipts= Receipt.objects.filter(vendor=vendor)
    context= {"receipts":receipts}
    return render(request,"vendors/receipts.html",context)