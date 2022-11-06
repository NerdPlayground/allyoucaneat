import json
import requests
from orders.models import Order
from django.urls import reverse
from django.conf import settings
from products.models import Content
from django.contrib import messages
from customers.decorators import is_customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect

def get_order(pk):
    return get_object_or_404(Order,pk=pk)

@login_required(login_url="user:login")
@is_customer
def extra_instructions(request,pk):
    order= get_order(pk)
    if request.method == "POST":
        extra_instructions= request.POST.get("extra-instructions")
        order.extra_instructions=extra_instructions if extra_instructions != "" else None
        order.save()
        return HttpResponseRedirect(reverse("orders:confirm-order",args=(order.id,)))
    context= {"product":order.product}
    return render(request,"orders/extra_instructions.html",context)

@login_required(login_url="user:login")
@is_customer
def confirm_order(request,pk):
    order= get_order(pk)
    contents= Content.objects.filter(orders=order)
    context= {
        "order":order,
        "contents":contents,
    }
    return render(request,"orders/confirm_order.html",context)

@login_required(login_url="user:login")
@is_customer
def delete_order(request,pk):
    order= get_order(pk)
    if request.method == "POST":
        order.delete()
        return HttpResponseRedirect(reverse("products:products"))
    context= {"obj":order}
    return render(request,"delete.html",context)